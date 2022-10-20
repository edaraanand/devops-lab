ReadWriteOnce
    the volume can be mounted as read-write by a single node. ReadWriteOnce access mode still can allow multiple pods to access the volume when the pods are running on the same node.
ReadOnlyMany
    the volume can be mounted as read-only by many nodes.
ReadWriteMany
    the volume can be mounted as read-write by many nodes.
ReadWriteOncePod
    the volume can be mounted as read-write by a single Pod. Use ReadWriteOncePod access mode if you want to ensure that only one pod across whole cluster can read that PVC or write to it. This is only supported for CSI volumes and Kubernetes version 1.22+.

RWO - ReadWriteOnce
ROX - ReadOnlyMany
RWX - ReadWriteMany
RWOP - ReadWriteOncePod