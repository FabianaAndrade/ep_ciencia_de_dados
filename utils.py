import pandas as pd
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt

def grafico_barras_target(df, coluna_1, coluna_2):
    grouped = df.groupby([coluna_1, coluna_2]).size().unstack(fill_value=0)
    proportions = grouped.div(grouped.sum(axis=1), axis=0) * 100
    proportions = proportions.sort_values(by='Dropout', ascending=False)

    fig, ax = plt.subplots(figsize=(10, 12))
    left = [0] * len(proportions)

    colors = {
        'Graduate': '#29af7f',
        'Dropout': '#0000FF'
    }

    for status in ['Graduate', 'Dropout']:
      ax.barh(proportions.index, proportions[status],
              left=left, label=status, color=colors[status])

      for i, (value, lft) in enumerate(zip(proportions[status], left)):
          if value > 5:
              ax.text(lft + value / 2, i, f'{value:.0f}%', ha='center', va='center', fontsize=9)

      left = [l + v for l, v in zip(left, proportions[status])]

    ax.set_xlabel("Porcentagem", fontsize=12)
    ax.set_ylabel(coluna_1, fontsize=12)
    ax.set_title(f"Distribuição dos alunos por status da conclusão do curso", fontsize=14)
    ax.legend(title="Status", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def grafico_barras(df, coluna):
    plt.figure(figsize=(5, 3))
    ax = sns.countplot(data=df, x=coluna, hue=coluna, palette='viridis', legend=False)

    plt.xlabel(coluna)
    plt.ylabel('Count')
    plt.title(f'Count de {coluna}')
    plt.xticks(rotation=90)

    for container in ax.containers:
        ax.bar_label(container, fontsize=10, padding=3)

    ax.margins(y=0.2)
    plt.tight_layout()
    plt.show()

def grafico_barras_horizontal(df, coluna):
    plt.figure(figsize=(6, 4))  # ligeiramente mais largo para nomes longos
    ax = sns.countplot(data=df, y=coluna, hue=coluna, palette='viridis', legend=False)

    plt.ylabel(coluna)
    plt.xlabel('Count')
    plt.title(f'Count de {coluna}')
    plt.yticks(rotation=0)

    for container in ax.containers:
        ax.bar_label(container, fontsize=10, padding=3)

    ax.margins(x=0.2)  # margem lateral agora no eixo x
    plt.tight_layout()
    plt.show()

def grafico_barras_proporcao(df, coluna_1, coluna_2):
  tabela = pd.crosstab(df[coluna_1], df[coluna_2])

  tabela.plot(kind='barh', stacked=True, figsize=(12, 7), colormap='viridis')
  plt.title(f' {coluna_1} X {coluna_2}')
  plt.xlabel('count')
  plt.ylabel(coluna_1)
  plt.legend(title= coluna_2, bbox_to_anchor=(1.05, 1), loc='upper left')
  plt.grid(True, axis='y', linestyle='--', alpha=0.7)
  plt.tight_layout()
  plt.show()

def grafico_boxplot(df, coluna):
    plt.figure(figsize=(4, 2))
    sns.boxplot(data=df, x=coluna, color='orchid')
    plt.title(f'Boxplot de {coluna}')
    plt.xlabel(coluna)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def grafico_distribuicao(df, coluna):
    plt.figure(figsize=(5, 3))
    sns.histplot(data=df, x=coluna, bins=20, kde=True, color='#29af7f')

    plt.xlabel(coluna)
    plt.ylabel('Count')
    plt.title(f'Distribuição de {coluna}')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def grafico_pizza(df, coluna):
    counts = df[coluna].value_counts()
    plt.figure(figsize=(4, 4))
    cores = ['#440154', '#29af7f']

    plt.pie(counts,
            labels=counts.index,
            autopct='%1.1f%%',
            startangle=90, colors = cores )
    plt.title(f'Distribuição de {coluna}')
    plt.axis('equal')
    plt.show()

application_mode = {
    1: "1st phase - general contingent",
    2: "Ordinance No. 612/93",
    5: "1st phase - special contingent (Azores Island)",
    7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99",
    15: "International student (bachelor)",
    16: "1st phase - special contingent (Madeira Island)",
    17: "2nd phase - general contingent",
    18: "3rd phase - general contingent",
    26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
    27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change of course",
    44: "Technological specialization diploma holders",
    51: "Change of institution/course",
    53: "Short cycle diploma holders",
    57: "Change of institution/course (International)"
}

previous_qualification  = {
    1: "Secondary education",
    2: "Higher education - bachelor's degree",
    3: "Higher education - degree",
    4: "Higher education - master's",
    5: "Higher education - doctorate",
    6: "Frequency of higher education",
    9: "12th year of schooling - not completed",
    10: "11th year of schooling - not completed",
    12: "Other - 11th year of schooling",
    14: "10th year of schooling",
    15: "10th year of schooling - not completed",
    19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
    38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    42: "Professional higher technical course",
    43: "Higher education - master (2nd cycle)"
}


matrial_status = {
    1: 'Single',
    2: 'Married',
    3: 'Widowed',
    4: 'Divorced',
    5: 'Facto Union',
    6: 'Legally separated',
}
Nacionality  = {
    1: "Portuguese",
    2: "German",
    6: "Spanish",
    11: "Italian",
    13: "Dutch",
    14: "English",
    17: "Lithuanian",
    21: "Angolan",
    22: "Cape Verdean",
    24: "Guinean",
    25: "Mozambican",
    26: "Santomean",
    32: "Turkish",
    41: "Brazilian",
    62: "Romanian",
    100: "Moldova (Republic of)",
    101: "Mexican",
    103: "Ukrainian",
    105: "Russian",
    108: "Cuban",
    109: "Colombian"
}
cursos_dict = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equiniculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)"
}

escolaridade_dict = {
    1: "Secondary Education—12th Year of Schooling or Equivalent",
    2: "Higher Education—bachelor’s degree",
    3: "Higher Education—degree",
    4: "Higher Education—master’s degree",
    5: "Higher Education—doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling—not completed",
    10: "11th Year of Schooling—not completed",
  11: "7th Year (Old)",
    12: "Other—11th Year of Schooling",
    13: "2nd year complementary high school course",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent",
    20: "Complementary High School Course",
    22: "Technical-professional course",
    25: "Complementary High School Course—not concluded",
    26: "7th year of schooling", #
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling—not completed",
    30: "8th year of schooling", #
    31: "General Course of Administration and Commerce",
    33: "Supplementary Accounting and Administration",
    34: "Unknown",
    35: "Cannot read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equivalent",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or equivalent",
    39: "Technological specialization course",
    40: "Higher education—degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education—master’s degree (2nd cycle)",
    44: "Higher Education—doctorate (3rd cycle)"
}

gender = {
    0: 'male',
    1: 'female'
}

internacional = {
    0: "no",
    1: "yes"
}

Debtor = {
    0: "no",
    1: "yes"
}

Tuition_fees_up_to_date = {
    0: "no",
    1: "yes"
}

Displaced = {
    0: "no",
    1: "yes"
}

educational_special_needs = {
    0: "no",
    1: "yes"
}

turno = {
    1: "daytime",
    0: "evening"
}



def colum_map(df):
  df["Mother's qualification"] = df["Mother's qualification"].map(escolaridade_dict)
  df["Father's qualification"] = df["Father's qualification"].map(escolaridade_dict)
  df["Course"] = df["Course"].map(cursos_dict)
  df['Marital status'] = df['Marital status'].map(matrial_status)
  df['Nacionality'] = df['Nacionality'].map(Nacionality)
  df['Gender'] = df['Gender'].map(gender)
  df['International'] = df['International'].map(internacional)
  df['Debtor'] = df['Debtor'].map(Debtor)
  df['Tuition fees up to date'] = df['Tuition fees up to date'].map(Tuition_fees_up_to_date)
  df['Displaced'] = df['Displaced'].map(Displaced)
  df['Educational special needs'] = df['Educational special needs'].map(educational_special_needs)
  df['Attendance'] = df['Attendance'].map(turno)
  df['Scholarship holder'] = df['Scholarship holder'].map(internacional)
  df['Application mode'] = df['Application mode'].map(application_mode)
  df['Previous qualification'] = df['Previous qualification'].map(previous_qualification)
  return df
