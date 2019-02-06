import pandas


def merge_runreg_runreg(runreg_dataframe1, runreg_dataframe2):
    return runreg_dataframe1.append(runreg_dataframe2, sort=True)


def merge_runreg_oms(runreg_dataframe, oms_dataframe):
    rr = runreg_dataframe.set_index(["run_number"])
    oms = oms_dataframe.set_index(["run_number"])
    return pandas.merge(
        rr, oms, how="left", left_on=["run_number"], right_on=["run_number"]
    ).reset_index()


def merge_runreg_tkdqmdoc(runreg_dataframe, tkdqmdoc_dataframe):
    rr = runreg_dataframe.set_index(["run_number", "reco"])
    tkdqm = tkdqmdoc_dataframe[
        [
            "run_number",
            "reco",
            "dataset",
            "reference_run_number",
            "reference_reco",
            "reference_runtype",
            "reference_dataset",
            "comment",
        ]
    ]
    tkdqm = tkdqm.set_index(["run_number", "reco"])

    # Remove Duplicates
    tkdqm = tkdqm[~tkdqm.index.duplicated(keep="first")]

    return pandas.merge(
        rr,
        tkdqm,
        how="left",
        left_on=["run_number", "reco"],
        right_on=["run_number", "reco"],
    ).reset_index()


def merge_runreg_tkdqmdoc_problem_runs(runreg_dataframe, tkdqmdoc_dataframe):
    rr = runreg_dataframe.set_index(["run_number", "reco"])
    tkdqm = tkdqmdoc_dataframe[["run_number", "reco", "problem_names"]]
    tkdqm = tkdqm.set_index(["run_number", "reco"])

    # Remove Duplicates
    tkdqm = tkdqm[~tkdqm.index.duplicated(keep="first")]

    return pandas.merge(
        rr,
        tkdqm,
        how="left",
        left_on=["run_number", "reco"],
        right_on=["run_number", "reco"],
    ).reset_index()
