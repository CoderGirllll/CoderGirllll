import cx_Freeze

executables = [cx_Freeze.Executable("Mini_Projects\python\Crash\crash.py")]

cx_Freeze.setup(
    name="Crash",
    options={"build_exe": {"packages": ["pygame", "random"],
                           "include_files":["Mini_Projects\python\Effects\\racecar.png",
                                            "Mini_Projects\python\Effects\\carIcon.png",
                                            "Mini_Projects\python\Effects\\crash.wav",
                                            "Mini_Projects\python\Effects\\backmusic.wav"
                                            ]}},
    executables = executables
)