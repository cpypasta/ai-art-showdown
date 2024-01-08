import solara, random

counter = solara.reactive(0)

@solara.component
def CounterDisplay():
    solara.Info(f"Counter: {counter}, Random: {random.randint(0, 100)}")
    
@solara.component
def IncrementButton():
    def increment():
        counter.value += 1
        
    solara.Button(label=f"Clicked: {counter}, Random: {random.randint(0, 100)}", on_click=increment)
    
@solara.component
def RandomText():    
    # does not get called when counter changes
    solara.Info(f"Random: {random.randint(0, 100)}")
    
@solara.component
def Page():
    IncrementButton()
    CounterDisplay()
    RandomText()