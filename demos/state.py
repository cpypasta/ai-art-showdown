import solara

# reactive variables, app-wide state
counter = solara.reactive(0)

def increment():
    counter.value += 1

@solara.component
def Counter():
    # uses a hook, local state
    count, set_count = solara.use_state(0)
    
    def increment():
        set_count(count + 1)
        
    solara.Info(f"Counter: {count}")
    solara.Button(label=f"Clicked: {count}", on_click=increment)

@solara.component
def Page():
    solara.Info(f"Counter: {counter}")
    solara.Button(label=f"Clicked: {counter}", on_click=increment)
    
    Counter()
    