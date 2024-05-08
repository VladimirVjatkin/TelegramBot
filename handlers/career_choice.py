from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.career_keyboard import make_keyboard


router = Router()


available_jobs = [
    'Программист',
    'Маркетолог',
    'Менеджер',
    'Аналитик',
    'Бухгалтер'
]
available_grades = [
    'Junior',
    'Middle',
    'Senior'
]
available_hair = [
    'Блондин',
    'Брюнет',
    'Шатен',
    'Лысый'
]
available_seler = [
    '50-100тыс руб',
    '100-200тыс руб',
    '200-400тыс руб',
    '400-800тыс руб'
]




class Choice(StatesGroup):
    job = State()
    grade = State()
    hair = State()
    seler = State()


@router.message(Command(commands=['profession']))
async def start(message: types.Message, state: FSMContext):
    await message.answer('Какая профессия вас интересует?', reply_markup=make_keyboard(available_jobs))
    await state.set_state(Choice.job)

@router.message(Choice.job, F.text.in_(available_jobs))
async def jobs(message: types.Message, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer('На каком уровне в этой профессии вы сейчас находитесь?', reply_markup=make_keyboard(available_grades))
    await state.set_state(Choice.grade)

@router.message(Choice.grade, F.text.in_(available_grades))
async def grades(message: types.Message, state: FSMContext):
    await state.update_data(grade=message.text)
    await message.answer('Очень важно знать ваш цвет волос, пожалуйста сообщите!', reply_markup=make_keyboard(available_hair))
    await state.set_state(Choice.hair)

@router.message(Choice.hair, F.text.in_(available_hair))
async def hair(message: types.Message, state: FSMContext):
    await state.update_data(hair=message.text)
    await message.answer('Сколько бы вы хотели зарабатывать??', reply_markup=make_keyboard(available_seler))
    await state.set_state(Choice.seler)

@router.message(Choice.job)
async def job_incorrectly(message: types.Message):
    await message.answer('Неправильно job. Попробуйте ещё раз', reply_markup=make_keyboard(available_jobs))

@router.message(Choice.grade)
async def grade_incorrectly(message: types.Message):
    await message.answer('Неправильно grade. Попробуйте ещё раз', reply_markup=make_keyboard(available_grades))

@router.message(Choice.hair)
async def hair_incorrectly(message: types.Message):
    await message.answer('Неправильно hair. Попробуйте ещё раз', reply_markup=make_keyboard(available_hair))


@router.message(Choice.seler, F.text.in_(available_seler))
async def seler(message: types.Message, state: FSMContext):
    await state.update_data(seler=message.text)
    await show_choices(message, state)
    await message.answer(f'Вы прошли весь тест господин {message.from_user.full_name}, \n с вами свяжутся наши HR',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

@router.message(Choice.seler)
async def seler_incorrectly(message: types.Message):
    await message.answer('Неправильно seler. Попробуйте ещё раз', reply_markup=make_keyboard(available_seler))

@router.message(Command(commands=['show_choices']))
async def show_choices(message: types.Message, state: FSMContext):
    user_data = await state.get_data()  # Получаем данные пользователя из контекста
    job = user_data.get('job', 'не выбрана')
    grade = user_data.get('grade', 'не выбран')
    hair = user_data.get('hair', 'не выбран')
    seler = user_data.get('seler', 'не выбран')

    await message.answer(f'Ваша выбранная профессия: {job}\nВаш уровень: {grade}\nВаш цвет волос: {hair}\nВаш требуемый уровень зарплаты: {seler}')  # Выводим выбор пользователя