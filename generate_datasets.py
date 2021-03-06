import scawg_util
import config
from logger import logger


def generate_data_on_variable(distribution, variable_name, values):
    for value in values:
        kwargs = config.get_default()
        kwargs[variable_name] = value
        generate_data(variable_name, distribution, **kwargs)

def generate_data(variable_name, distribution, instance_num=None, worker_num_per_instance=None, task_num_per_instance=None,
                  task_duration=(1, 2), task_requirement=(1, 3), task_confidence=(0.75, 0.8), worker_capacity=(2, 3),
                  worker_reliability=(0.75, 0.8), working_side_length=(0.05, 0.1), batch_interval_time=120, worker_location_mean=0.5,
                worker_location_variance=0.05, worker_cluster_number=3, worker_speed=0.25):

    """
        generate data according to settings
        :type distribution: str
        :type instance_num: int
        :type worker_num_per_instance: int
        :type task_num_per_instance: int
        :type task_duration: tuple
        :type task_requirement: tuple
        :type task_confidence: tuple
        :type worker_capacity: tuple
        :type worker_reliability: tuple
        :type working_side_length: tuple
        :type batch_interval_time: double
        :type worker_speed: double
    """
    logger.info('generating data')
    if distribution == 'real':
        total_real_data_time_length = 3600
        instance_num = total_real_data_time_length/batch_interval_time

    if variable_name == 'worker_location_mean' or variable_name == 'worker_location_variance':
        worker_cluster_number = 0

    if variable_name == 'worker_num_per_instance' or variable_name == 'task_num_per_instance':
        worker_cluster_number = -1

    scawg_util.generate_general_task_and_worker(variable_name, distribution, [
        distribution,
        'general',
        'instance=' + str(instance_num),
        'worker_num_per_instance=' + str(worker_num_per_instance),
        'task_num_per_instance=' + str(task_num_per_instance),
        'min_task_duration=' + str(task_duration[0]),
        'max_task_duration=' + str(task_duration[1]),
        'min_task_requirement=' + str(task_requirement[0]),
        'max_task_requirement=' + str(task_requirement[1]),
        'min_task_confidence=' + str(task_confidence[0]),
        'max_task_confidence=' + str(task_confidence[1]),
        'min_worker_capacity=' + str(worker_capacity[0]),
        'max_worker_capacity=' + str(worker_capacity[1]),
        'min_worker_reliability=' + str(worker_reliability[0]),
        'max_worker_reliability=' + str(worker_reliability[1]),
        'min_working_side_length=' + str(working_side_length[0]),
        'max_working_side_length=' + str(working_side_length[1]),
        'batch_interval_time=' + str(batch_interval_time),
        'worker_location_mean=' + str(worker_location_mean),
        'worker_location_variance=' + str(worker_location_variance),
        'worker_cluster_number=' + str(worker_cluster_number),
        'worker_speed=' + str(worker_speed)
    ])
    logger.info('data generated')


if __name__ == '__main__':
    for dist in config.distribution:
        if dist != 'real':
            # generate_data_on_variable(dist, 'worker_num_per_instance', config.worker_num_per_instance)
            # generate_data_on_variable(dist, 'task_num_per_instance', config.task_num_per_instance)
            generate_data_on_variable(dist, 'worker_location_mean', config.worker_location_mean)
            generate_data_on_variable(dist, 'worker_location_variance', config.worker_location_variance)
            generate_data_on_variable(dist, 'worker_cluster_number', config.worker_cluster_number)
        else:
            # generate_data_on_variable(dist, 'task_duration', config.task_duration)
            # generate_data_on_variable(dist, 'task_requirement', config.task_requirement)
            # generate_data_on_variable(dist, 'task_confidence', config.task_confidence)
            # generate_data_on_variable(dist, 'worker_capacity', config.worker_capacity)
            # generate_data_on_variable(dist, 'worker_reliability', config.worker_reliability)
            # generate_data_on_variable(dist, 'working_side_length', config.working_side_length)
            # generate_data_on_variable(dist, 'batch_interval_time', config.batch_interval_time)
            generate_data_on_variable(dist, 'worker_speed', config.worker_speed)
