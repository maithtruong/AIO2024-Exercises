import numpy as np


def create_train_data():

    data_options = [['Sunny', 'Overcast', 'Rain'],
                    ['Hot', 'Cool', 'Mild'],
                    ['High', 'Normal'],
                    ['Weak', 'Strong'],
                    ['no', 'yes']]

    data = []

    for _ in range(10):
        obi_values = []
        for feature_options in data_options:
            obi_featurej_value = np.random.choice(feature_options)
            obi_values.append(obi_featurej_value)
        data.append(obi_values)

    return np.array(data)


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))

    total_obs = len(train_data)

    for index, label in enumerate(y_unique):
        count = 0
        for obs in train_data:
            if obs[4] == label:
                count += 1
        label_prob = count / total_obs
        prior_probability[index] = label_prob

    return prior_probability


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = {label: {} for label in y_unique}
    list_x_name = []

    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        for label in y_unique:
            conditional_probability[label][i] = []
            for x in x_unique:
                p_x_given_y = np.sum(
                    (train_data[:, -1] == label) & (train_data[:, i] == x)) / np.sum(train_data[:, -1] == label)
                conditional_probability[label][i].append((x, p_x_given_y))

    return conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    list_features = np.array(list_features)
    indices = np.nonzero(list_features == feature_name)[0]

    if indices.size == 0:
        raise ValueError(f"Feature name '{feature_name}' not found in list_features")

    return indices[0]

def train_naive_bayes(train_data):
    y_unique = ['no', 'yes']
    prior_probability = compute_prior_probability(train_data)

    conditional_probability, list_x_name = compute_conditional_probability(train_data
                                                                           )
    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x_indices = [get_index_from_value(feature, list_x_name[i])
                 for i, feature in enumerate(X)]

    p0 = prior_probability[0]
    p1 = prior_probability[1]

    for i, x_index in enumerate(x_indices):
        if x_index < len(conditional_probability['no'][i]):
            feature_prob = dict(conditional_probability['no'][i]).get(
                x_index, (None, 1))[1]
            p0 *= feature_prob

        if x_index < len(conditional_probability['yes'][i]):
            feature_prob = dict(conditional_probability['yes'][i]).get(
                x_index, (None, 1))[1]
            p1 *= feature_prob

    y_pred = 1 if p1 > p0 else 0

    return y_pred


def main():
    # 4.1
    train_data = create_train_data()
    print(train_data)

    # 4.2
    prior_probability = compute_prior_probability(train_data)
    print('P(play tennis = No)', prior_probability[0])
    print('P(play tennis = Yes)', prior_probability[1])

    # 19
    X = ['Sunny', 'Cool', 'High', 'Strong']
    data = create_train_data()
    prior_probability, conditional_probability, list_x_name = train_naive_bayes(
        data)
    pred = prediction_play_tennis(
        X, list_x_name, prior_probability, conditional_probability)

    if pred:
        print("Ad should go!")
    else:
        print("Ad should not go!")

if __name__ == "__main__":
    main()
