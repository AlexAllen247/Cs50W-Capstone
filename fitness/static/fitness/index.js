function updateExercise(exercise_id) {
    fetch(`/exercises_api/id/${exercise_id}`)
        .then(response => {
            if (response.ok) { console.log("HTTP request successful") }
            else { console.log("HTTP request unsuccessful") }
            return response
        })
        .then(response => response.json())
        .then(exercise => {
            document.querySelector(`#exercise_${exercise.id}`).innerHTML = `
                            <td><input class="form-control sm" id="exercise_info" rows="1" value="${exercise.exercise_info}" /></td>
                            <span><button type="button" id="save_exercise" onclick="saveExercise(${exercise.id})" class="btn btn-primary btn-sm">Save</button></span>`;
        })
        .catch(error => {
            console.log("error: ", error);
        });
}

function saveExercise(exercise_id) {
    const exercise_info = document.querySelector("#exercise_info").value;
    const request = new Request(`/exercises_api/save/${exercise_id}`,);
    alert('Exercise Saved, Congratulations on improving on this exercise! Keep up the Great Work!')
    fetch(request, {
        method: 'PUT',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            exercise_info: exercise_info
        })
    })
        .then(response => {
            if (response.ok) { console.log("HTTP request successful") }
            else { console.log("HTTP request unsuccessful") }
            return response
        })
        .then(response => response.json())
        .then(exercise => {
            document.querySelector('#save_exercise').style.display = 'none';
            document.querySelector('#exercise_info').style.display = 'block';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}