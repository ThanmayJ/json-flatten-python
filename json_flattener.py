def flatten(data, seperator = '.'):
    output = {}

    def flatten_helper(data, idx):
        if isinstance(data, dict):
            keys = list(data.keys())
            if keys:
                for key in keys:
                    flatten_helper(data[key], idx+key+seperator)
            else:
                output[idx[:-1*len(seperator)]] = data
        elif isinstance(data, list):
            if data:
                for i in range(len(data)): 
                    flatten_helper(data[i], idx+f'[{i}]'+seperator)
            else:
                output[idx[:-1*len(seperator)]] = []
        else:
            output[idx[:-1*len(seperator)]] = data
    
    flatten_helper(data, '')
    
    return output





def unflatten(data, seperator = '.'):
    if isinstance(data, dict):
        f_keys = list(data.keys())
        if f_keys[0].split(seperator)[0][0] == '[' and f_keys[0].split(seperator)[0][-1] == ']':
            output = []
        else:
            output = {}

    def unflatten_helper(data, f_keys):
        for f_key in f_keys:
            val = data[f_key]
            keys = f_key.split(seperator)
            i = 0
            x = output
            while i < len(keys) - 1:
                if isinstance(x, dict):
                    try:
                        x = x[keys[i]]
                    except KeyError:
                            if keys[i+1][0] == '[' and keys[i+1][-1] == ']':
                                x[keys[i]] = []
                            else:
                                x[keys[i]] = {}
                            x = x[keys[i]]
                elif isinstance(x, list):
                    if keys[i+1][0] == '[' and keys[i+1][-1] == ']':
                        try:
                            x = x[int(keys[i+1][1:-1])]
                        except IndexError:
                            x.append([])
                            x = x[int(keys[i+1][1:-1])]
                    else:
                        try:
                            x = x[int(keys[i][1:-1])]
                        except IndexError:
                            x.append({})
                            x = x[int(keys[i][1:-1])]
                i+=1
            
            if isinstance(x, list):
                x.append(val) 
            else:   
                x[keys[-1]] = val
    
    unflatten_helper(data, f_keys)
    
    return output  
