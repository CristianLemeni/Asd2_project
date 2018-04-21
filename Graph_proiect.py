def dijkstra(graph,source,destination,visited=[],distances={},predecessors={}):
    if source == destination:
        # Se creaza drumul si se afiseaza
        path=[]
        pred=destination
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('shortest path: '+str(path)+" cost="+str(distances[destination])) 
    else :     
        # daca este drumul initial, initializam costul
        if not visited: 
            distances[source]=0
        # parcurgem graph-ul(vecinii)
        for neighbor in graph[source] :
            if neighbor not in visited:
                new_distance = distances[source] + graph[source][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = source
        # marcam pe cei vizitati
        visited.append(source)
        # dupa ce s-a terminat procesul, algoritmul ruleaza cu cel mai scurt traseu
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,destination,visited,distances,predecessors)
        


if __name__ == "__main__":


	graph = {'intrare': {'hol SE I': 1, 'AM': 3, 'hol SV I': 1},
				'hol SE I': {'intrare': 1, 'hol SE II': 1, 'hol NE I': 6,'A02': 3.5,'A01': 1, '001': 1, '002': 2, '003': 3, '004': 4},
						'001': {'hol SE I': 1}, '002': {'hol SE I': 2}, '003': {'hol SE I': 3}, '004' : {'hol SE I': 4}, 'A01' : {'hol SE I': 1}, 'A02' : {'hol SE I': 3.5, 'hol Ne': 5},
				'hol SE II' : {'hol SE I': 1, 'hol NE II': 6,'A03': 3.5, '005': 1, '006' : 2, 'F.Fizica' : 3, 'Caserie' : 4},
					'A03': {'hol SE II': 3.5, 'hol NE II' : 5}, '005' : {'hol SE II': 1}, '006' :{'hol SE II': 2}, 'F.Fizica' : {'hol SE II': 3}, 'Caserie' : {'hol SE II': 4},
				'AM' : {'hol NE I' : 1, 'hol NV I' : 1, 'intrare' : 3},
				'hol NE I' : {'AM' : 1, '032' : 1, '031' : 2, '029' : 3, 'hol NE II' : 1, 'hol SE I' : 6, 'A02' : 5},
					'032' : {'hol NE I' : 1}, '031' : {'hol NE I': 2}, '029' : {'hol NE I':3},
				'hol NE II' : {'028' : 1, '027' : 2, '026' : 3, 'baie' : 4, 'hol SE II' : 6, 'A03' : 5},
					'028' :{'hol NE II' : 1}, '027': {'hol NE II' : 2}, '026': {'hol NE II' : 3}, 'baie': {'hol NE II': 4},
				'hol SV I' : {'infragrid': 1, '050b': 2, 'lift si scari' : 2, 'hol SV II': 1},
					'infragrid':{'hol SV I' :1}, '050b': {'hol SV I' :2}, 'lift si scari' : {'hol SV I' :2},
				'hol SV II' : {'050a': 3, '048': 1, '047': 2, '046a': 3, '046b':4, '045a':5, 'e-Austria': 6, 'hol la dreapta': 6},
					'hol la dreapta' : {'hol SV II': 6, '045c': 2, '045d': 2}, '045c':{'hol la dreapta':2}, '045d':{'hol la dreapta':2},
					'050a':{'hol SV II': 3}, '048': {'hol SV II': 1}, '047': {'hol SV II': 2}, '046a': {'hol SV II': 3}, '046b':{'hol SV II': 4}, '045a':{'hol SV II': 5}, 'e-Austria': {'hol SV II': 6},
				'hol NV I' : {'AM': 1, '036': 1, 'uvt Tv 1': 2, 'uvt Tv 2': 3, 'hol NV II': 2},
					'036':{'hol NV I': 1}, 'uvt Tv 1': {'hol NV I': 2}, 'uvt Tv 2': {'hol NV I': 3},
				'hol NV II' : {'baie B': 1, 'baie F': 3, 'hol intermediar': 1, 'hol NV I': 2},
					'baie B':{'hol NV II':1}, 'baie F':{'hol NV II':3},
					'hol intermediar' : {'iesire': 2, 'lectoratul francez': 1, '042': 2, '043': 3, '044': 4, 'hol NV II': 1},
						'iesire':{'hol intermediar': 2}, 'lectoratul francez':{'hol intermediar': 1}, '042': {'hol intermediar': 2}, '043': {'hol intermediar': 3}, '044':{'hol intermediar': 4}}
	dijkstra(graph,'iesire','intrare')#graph/destinationinatie/start