import pyautogui


nome_XY = pyautogui.locateCenterOnScreen('./semana7/campo_nome.png', confidence=0.9 )
pyautogui.click(nome_XY, duration=0.5)
pyautogui.write('Rafael Clebson Franco Junior', interval=0.2)

cpf_XY = pyautogui.locateCenterOnScreen('./semana7/campo_cpf.png', confidence=0.9 )
pyautogui.click(cpf_XY, duration=0.5)
pyautogui.write('14613028620', interval=0.2)

sim_XY = pyautogui.locateCenterOnScreen('./semana7/campo_sim.png', confidence=0.9 )
pyautogui.click(sim_XY, duration=0.5)

enviar_XY = pyautogui.locateCenterOnScreen('./semana7/campo_enviar.png', confidence=0.9 )
pyautogui.click(enviar_XY, duration=0.5)
