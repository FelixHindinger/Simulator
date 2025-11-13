from simulation_modes import test_mode
import os
# from experiments import plotting
from metrics import anonymity_metrics
import pandas as pd
import json


if __name__ == "__main__":

	# try:

	print("Mix-network Simulator\n")
	print("Insert the following network parameters to test: ")

	with open('test_config.json') as json_file:
		config = json.load(json_file)

	if not os.path.exists('./playground_experiment/logs'):
		os.makedirs('./playground_experiment/logs')
	else:
		try:
			os.remove('./playground_experiment/logs/packet_log_latency.csv')
			os.remove('./playground_experiment/logs/packet_log_anonymity.csv')
			os.remove('./playground_experiment/logs/last_mix_entropy_latency.csv')
			os.remove('./playground_experiment/logs/last_mix_entropy_anonymity.csv')
		except:
			pass

	test_mode.run(exp_dir='playground_experiment', conf_file=None, conf_dic=config)
	throughput = test_mode.throughput

	packetLogsDir_latency = './playground_experiment/logs/packet_log_latency.csv'
	entropyLogsDir_latency = './playground_experiment/logs/last_mix_entropy_latency.csv'
	packetLogsDir_anonymity = './playground_experiment/logs/packet_log_anonymity.csv'
	entropyLogsDir_anonymity = './playground_experiment/logs/last_mix_entropy_anonymity.csv'
	packetLogs_latency = pd.read_csv(packetLogsDir_latency, delimiter=';')
	entropyLogs_latency = pd.read_csv(entropyLogsDir_latency, delimiter=';')
	packetLogs_anonymity = pd.read_csv(packetLogsDir_anonymity, delimiter=';')
	entropyLogs_anonymity = pd.read_csv(entropyLogsDir_anonymity, delimiter=';')

	unlinkability = anonymity_metrics.getUnlinkability(packetLogs_latency)
	entropy_latency = anonymity_metrics.getEntropy(entropyLogs_latency, config["misc"]["num_target_packets"])
	latency_latency = anonymity_metrics.computeE2ELatency(packetLogs_latency)
	entropy_anonymity = anonymity_metrics.getEntropy(entropyLogs_anonymity, config["misc"]["num_target_packets"])
	latency_anonymity = anonymity_metrics.computeE2ELatency(packetLogs_anonymity)

	print("\n\n")
	print("Simulation finished. Below, you can check your results.")
	print("-------------------------------------------------------")
	print("-------- Anonymity metrics --------")
	print(">>> Entropy for low latency traffic: ", entropy_latency)
	print(">>> Entropy for high anonymity traffic: ", entropy_anonymity)
	if unlinkability[0] == None:
		print(">>> E2E Unlinkability: epsilon= -, delta=%f)" % unlinkability[1])
	else:
		print(">>> E2E Unlinkability: (epsilon=%f, delta=%f)" % unlinkability)
	print("\n\n")
	print("-------- Performance metrics --------")
	print(">> Overall latency for low latency traffic: %f seconds (including mixing delay and packet cryptographic processing)" % (latency_latency))
	print(">> Overall latency for high anonymity traffic: %f seconds (including mixing delay and packet cryptographic processing)" % (latency_anonymity))
	print(">> Throuhput of the network: %f [packets / second]" % throughput)
	print("-------------------------------------------------------")

	# except Exception as e:
		# print(e)
		# print("Something went wrong! Check whether your input parameters are correct.")
