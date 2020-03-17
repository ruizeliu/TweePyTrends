
import util

###### Crawler ######


def crawler(key, info_tuple, max = 5):
	'''
	max: maxmium trails allowed (suggest: 5)
	'''
	queue = [key]
	path = []
	i = 1
	dic = {}

	while len(queue) > 0 and i <= max:
		key = queue[0]
		queue.remove(key)
		path.append(key)
		web = util.retrieve_web(key, info_tuple)
		hashtag = util.process_hashtag(web)
		text = util.process_text(web)
		queue.extend([x for x in set(hashtag) if x != key and x not in queue and x not in path])
		dic.update({key: [hashtag, text]})

		i += 1

	return dic
