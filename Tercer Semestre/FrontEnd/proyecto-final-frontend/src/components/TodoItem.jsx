export function TodoItem({todo, cambiarEstado}){
	const {id, task, completed} = todo;

	const funcionCambiarEstado = () => {
		cambiarEstado(id);
	}

	return <>
			<li className="list-group-item">
				<input className="form-check-input me-2" type="checkbox" onChange={funcionCambiarEstado} checked = {completed} />{task}
			</li>
	</>
}