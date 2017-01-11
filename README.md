<snippet>
  <content><![CDATA[
# ${1:Efficient Measurement of Complex Networks Using Link Queries}
—Complex networks are at the core of an intense research activity. However, in most cases, intricate and costly measurement procedures are needed to explore their structure. In some cases, these measurements rely on link queries: given two nodes, it is possible to test the existence of a link between them. These tests may be costly, and thus minimizing their number while maximizing the number of discovered links is a key issue. This is a challenging task, though, as initially no information is known on the network. This paper studies this problem: we observe that properties classically observed on real-world complex networks give hints for their efficient measurement; we derive simple principles and several measurement strategies based on this, and experimentally evaluate their efficiency on real-world cases. In order to do so, we introduce methods to evaluate the efficiency of strategies. We also explore the bias that different measurement strategies may induce.
## Installation
You need to have the following libraries:
  - Networkx
  - re
## Usage
`python simul -f <input_graph> -o <output_measurments> -n <#_rand_phase> -t <strategie_name:{TBF, TBFC, Complete, V-random,..}>`

Or check the help included:

`python simul.py -h`
## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
]]></content>
  <tabTrigger>readme</tabTrigger>
</snippet>
