import { TodoItem } from "./TodoItem";
import { useEffect, useRef, useState } from "react";
import { v4 as uuidv4 } from 'uuid';

// definición de KEY
const KEY = 'todoList-todo';

export function TodoList(){
	// hooks de react <>
	// const que esta llamando a useState
	
	
	const [todos, setTodos] = useState(
		[
			// primer objeto del arreglo todos
			{id: 1, task: "Estudiar Programación", completed: false},
			{id: 2, task: "Estudiar base de datos", completed: false},
			{id: 3, task: "Estudiar Ingles", completed: true},
		]
	);
	// constante que se encarga de guardar la referencia de un elemento
	const taskRef = useRef();
	
	// obtiene datos de KEY en localStorage
	useEffect(
		() => {
			const tareasAlmacenadas = JSON.parse(localStorage.getItem(KEY));
			// Si hay tareas almacenadas en localStorage las setea
			if(tareasAlmacenadas)
				setTodos(tareasAlmacenadas)
		}, []
	);

	// obtiene archivo local storage, luego setea cambia los datos del local storage
	// cada vez que haya movimiento en los todos, el useffect salta, toma los objetos los conv en json y los setea en local storage
	useEffect(
		() => {
			localStorage.setItem(KEY, JSON.stringify(todos));
		}, [todos]
	)


	// funcion que se encarga de agregar una tarea
	const agregarTarea = () => {
		console.log("Estamos llamando a la funcion a agregar");
		console.log(taskRef.current.value);
		console.log(uuidv4());
		const task = taskRef.current.value;
		if(task === '') return;

		// setTodos es la funcion que se encarga de modificar el estado de la variable todos
		setTodos(
			// prevTodos es el arreglo de todos
			(prevTodos) => {
				// constante que se encarga de guardar el ultimo elemento del arreglo
				const newtask = {
					// uuid para crear un hash unico
					id: uuidv4(),
					task: task,
					completed: false
				}
				// sintaxis de spread operator: los 3 puntos ... se encargan de desglosar el arreglo prevTodos
				return [...prevTodos, newtask]
			}
		)
		taskRef.current.value = null;
		}
	// Elimina tareas completadas
	const eliminarTarea = () => {
		const newTodos = todos.filter((todo) => !todo.completed);
		setTodos(newTodos);

	}





	// linea32: funcion map hace un recorrido de todos los elementos del arreglo
	// uuid para crear un hash unico
	
	// funcion que se encarga de contar la cantidad de tareas falsas
	const cantidadTareas = ()=>{
		// filter se encarga de filtrar los elementos del arreglo
		return todos.filter((todo) => !todo.completed).length;
	
	};

	const resumenTareas = () => {
		const cantidad = cantidadTareas();
		let mensaje = ``;
		let classAlert = ``;

		if (cantidad === 0){
			mensaje = "Felicidades! no hay tareas pendientes";
			classAlert = "alert alert-success";
		}else if (cantidad === 1){
			mensaje = "Hay 1 tarea pendiente";
			classAlert = "alert alert-warning";
		}else if (cantidad > 1){
			mensaje = `Hay ${cantidad} tareas pendientes`;
			classAlert = "alert alert-danger";
		}

		return (
			<div className="row mt-3">
				<div className="col-md-12">
					<div className={classAlert}>
						{mensaje}
					</div>
				</div>
			</div>
		)
	};

	const cambiarEstadoTarea= (id) => {
		// Tomar todas las tareas y las guardo en newTodos
		const newTodos = [...todos];
		// Buscar la tarea que se quiere cambiar
		const todo = newTodos.find((todo) => todo.id === id);
		todo.completed = !todo.completed;
		setTodos(newTodos);
	};

	return <>
		<div className="row">
			<div className="col-md-12">
				<h1>Lista de tareas</h1>
				<div className="input-group mb-3">
					<input type="text" className="form-control" id="inputTask" ref={taskRef} placeholder="Ingrese una tarea"/>
					<button type="submit" className="btn btn-success" onClick={agregarTarea} ><i className="bi bi-plus-circle-fill"></i></button>
					<button type="submit" className="btn btn-danger" onClick={eliminarTarea} ><i className="bi bi-trash-fill"></i></button>
				</div>
			</div>
		</div>
		<div className="row">
			<div className="col-md-12">
				<ul className="list-group">
					{todos.map(
						(todo) => {return <TodoItem todo = {todo} key={todo.id} cambiarEstado = {cambiarEstadoTarea	}/>}
					)
					}
				</ul>
			</div>
		</div>
		{resumenTareas()}
	</>
}