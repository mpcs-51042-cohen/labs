# Write a function that takes a large body of text and returns a dictionary of
# word frequencies.  For example, the sentence "To be or not to be, that is the question."
# would return a dictionary like this: 
# { "to": 2, "be", 2, "or": 1, "not": 1, "that": 1, "is": 1, "the": 1, "question": 1 }

def freq_count(text):
  # REPLACE THIS CODE 
  return { } 
  
  

story = """Volcanoes are powerful geological features that shape our planet. A volcano forms when magma from beneath the Earth's crust reaches the surface. When magma emerges from a volcano, we call it lava. Lava flows can travel great distances from the volcano's crater.
The magma inside a volcano contains dissolved gases. As magma rises, pressure decreases, and gases expand. This pressure buildup can cause explosive eruptions. Some volcanoes erupt violently, while other volcanoes erupt more gently. The type of eruption depends on the magma's composition.
Volcanic eruptions release not only lava but also ash and volcanic gases. Ash clouds from volcanic eruptions can affect air travel and climate. The ash falls back to earth, enriching the soil. Many volcanic regions have fertile soil because of this ash.
Scientists study volcanoes to predict eruptions and protect nearby communities. They monitor pressure changes, gas emissions, and ground deformation around the volcano. Understanding volcanic behavior helps scientists issue warnings before dangerous eruptions occur.
Despite their dangers, volcanoes create new land and provide geothermal energy. The volcanic islands of Hawaii demonstrate how volcanoes build landmasses over time. Volcanoes remain among nature's most fascinating and powerful phenomena."""

print(freq_count(story))

# EXPECTED RESULT:
# {'volcanoes': 8, 'volcanic': 6, 'magma': 5, 'eruptions': 5, 'volcano': 5, 'ash': 4, 'lava': 3, 'pressure': 3, 'gases': 3, 'the': 3, 'from': 3, 'and': 3, 'erupt': 2, 'scientists': 2, 'soil': 2, 'a': 2, 'when': 2, 'we': 2, 'can': 2, 'of': 2, 'this': 2, 'understanding': 2, 'powerful': 2, 'are': 1, 'geological': 1, 'features': 1, 'that': 1, 'shape': 1, 'our': 1, 'planet': 1, 'forms': 1, 'beneath': 1, "earth's": 1, 'crust': 1, 'reaches': 1, 'surface': 1, 'emerges': 1, 'call': 1, 'it': 1, 'flows': 1, 'travel': 1, 'great': 1, 'distances': 1, "volcano's": 1, 'crater': 1, 'inside': 1, 'contains': 1, 'dissolved': 1, 'as': 1, 'rises': 1, 'decreases': 1, 'expand': 1, 'buildup': 1, 'cause': 1, 'explosive': 1, 'some': 1, 'violently': 1, 'while': 1, 'other': 1, 'more': 1, 'gently': 1, 'type': 1, 'eruption': 1, 'depends': 1, 'on': 1, "magma's": 1, 'composition': 1, 'release': 1, 'not': 1, 'only': 1, 'but': 1, 'also': 1, 'clouds': 1, 'affect': 1, 'air': 1, 'travel': 1, 'climate': 1, 'falls': 1, 'back': 1, 'to': 1, 'earth': 1, 'enriching': 1, 'many': 1, 'regions': 1, 'have': 1, 'fertile': 1, 'because': 1, 'study': 1, 'predict': 1, 'protect': 1, 'nearby': 1, 'communities': 1, 'they': 1, 'monitor': 1, 'changes': 1, 'gas': 1, 'emissions': 1, 'ground': 1, 'deformation': 1, 'around': 1, 'behavior': 1, 'helps': 1, 'issue': 1, 'warnings': 1, 'before': 1, 'dangerous': 1, 'occur': 1, 'despite': 1, 'their': 1, 'dangers': 1, 'create': 1, 'new': 1, 'land': 1, 'provide': 1, 'geothermal': 1, 'energy': 1, 'islands': 1, 'hawaii': 1, 'demonstrate': 1, 'how': 1, 'build': 1, 'landmasses': 1, 'over': 1, 'time': 1, 'remain': 1, 'among': 1, "nature's": 1, 'most': 1, 'fascinating': 1, 'phenomena': 1}
