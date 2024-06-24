def calc_dis_p2p(p1, p2):
    sum_square = 0
    for d1, d2 in zip(p1, p2):
        sum_square += (d1 - d2) ** 2
    dis = sum_square ** 0.5
    return dis

def assign_labels(samples, labels, clusters):
    for i, sample in enumerate(samples):
        min_dis = 100
        min_cluster = -1
        for j, cluster in enumerate(clusters):
            dis = calc_dis_p2p(sample, cluster)
            if dis < min_dis:
                min_dis = dis
                min_cluster = j
        labels[i] = min_cluster
    return labels

def update_clusters(samples, labels, clusters):
    for i in range(len(clusters)):
        cluster_belong_samples = []
        for j, label in enumerate(labels):
            if label == i:
                cluster_belong_samples.append(samples[j])

        # If no sample belongs to the cluster, skip this cluster
        if len(cluster_belong_samples) == 0:
            continue

        # Else, update the cluster
        else:
            new_cluster = [0] * len(clusters[0])
            for sample in cluster_belong_samples:
                for k in range(len(sample)):
                    new_cluster[k] += sample[k]
            for k in range(len(new_cluster)):
                new_cluster[k] /= len(cluster_belong_samples)
            clusters[i] = new_cluster
    return clusters

def kmean_iteration(samples, labels, clusters):
    # assign labes
    labels = assign_labels(samples, labels, clusters)

    # update clusters
    clusters = update_clusters(samples, labels, clusters)

    return samples, labels, clusters

samples = [[1, 3], [7, 6], [2, 2], [8, 6], [9, 6], [1, 1], [7, 5], [8, 5], [2, 3]]
labels = len(samples) * [-1]
clusters = [[3, 7], [4, 3]]

# # iteration 1
# samples, labels, clusters = kmean_iteration(samples, labels, clusters)
# print(clusters)

# # iteration 2
# samples, labels, clusters = kmean_iteration(samples, labels, clusters)
# print(clusters)

# # iteration 3
# samples, labels, clusters = kmean_iteration(samples, labels, clusters)
# print(clusters)

current_cluster = clusters
while True:
    samples, labels, clusters = kmean_iteration(samples, labels, clusters)
    if current_cluster == clusters:
        break
    current_cluster = clusters

print(f'Final clusters: {clusters}')