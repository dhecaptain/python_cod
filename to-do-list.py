import streamlit as st

def app(tasks):
    st.title("To-Do List")
    task = st.text_input("Add a task:")
    if st.button("Add"):
        tasks.append({"task": task, "completed": False})

    if st.button("Clear"):
        tasks.clear()

    st.write("## Tasks")
    for i, task in enumerate(tasks):
        completed = st.checkbox("", value=task["completed"])
        task["completed"] = completed
        st.write(f"{i+1}. {task['task']}")

    if len(tasks) > 0:
        completed_tasks = [task for task in tasks if task["completed"]]
        incomplete_tasks = [task for task in tasks if not task["completed"]]
        if len(completed_tasks) > 0:
            st.write(f"## Completed Tasks ({len(completed_tasks)})")
            for i, task in enumerate(completed_tasks):
                st.write(f"{i+1}. {task['task']}")
        if len(incomplete_tasks) > 0:
            st.write(f"## Incomplete Tasks ({len(incomplete_tasks)})")
            for i, task in enumerate(incomplete_tasks):
                st.write(f"{i+1}. {task['task']}")

if __name__ == "__main__":
    tasks = []
    app(tasks)
