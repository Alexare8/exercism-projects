class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records: list[Record]) -> Node | None:
    root = None
    nodes = []
    records.sort(key=lambda x: x.record_id)
    if [i.record_id for i in records] != list(range(len(records))):
        raise ValueError("Record id is invalid or out of order.")
    for record in records:
        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")
        if record.record_id != 0 and record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")

        node = Node(record.record_id)
        nodes.append(node)
        if node.node_id == 0:
            root = node
        else:
            nodes[record.parent_id].children.append(node)
    return root
