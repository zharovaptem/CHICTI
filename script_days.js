function populateHoursSelect() {
    const hourSelect = document.getElementById('hourSelect');
    for (let hour = 0; hour <= 23; hour++) {
        let option = document.createElement('option');
        option.value = hour;
        option.textContent = hour.toString().padStart(2, '0');
        hourSelect.appendChild(option);
    }
}


function populateMinutesSelect() {
    const minuteSelect = document.getElementById('minuteSelect');
    for (let minute = 0; minute <= 59; minute++) {
        let option = document.createElement('option');
        option.value = minute;
        option.textContent = minute.toString().padStart(2, '0');
        minuteSelect.appendChild(option);
    }
}

//Обработка функций при запуске окна в браузере
window.onload = function() {
    populateHoursSelect();
    populateMinutesSelect();
};

document.getElementById('addTask').addEventListener('click', function() {
    const hourSelect = document.getElementById('hourSelect');
    const minuteSelect = document.getElementById('minuteSelect');
    const taskInput = document.getElementById('taskInput').value;

    const hourValue = parseInt(hourSelect.value);
    const minuteValue = parseInt(minuteSelect.value);

    if (hourValue >= 0 && hourValue <= 23 && minuteValue >= 0 && minuteValue <= 59) {
        // Создание нового элемента задачи
        const timeSlot = document.createElement('div');
        timeSlot.className = 'time-slot';
        const label = document.createElement('label');
        label.textContent = `${hourValue}:${minuteValue}`;
        label.className = 'time-place';
        const input = document.createElement('label');
        input.textContent = `${taskInput}`;
        input.className = 'text-place';
        input.placeholder = ``;

        timeSlot.appendChild(label);
        timeSlot.appendChild(input);
        timeSlots.appendChild(timeSlot);

        // Очистка полей ввода после добавления задачи
        document.getElementById('taskInput').value = '';
        hourSelect.selectedIndex = 0; // Сброс выбора часов на значение по умолчанию
        minuteSelect.selectedIndex = 0; // Сброс выбора минут на значение по умолчанию
    } else {
        alert('Пожалуйста, введите корректное время.');
    }
});