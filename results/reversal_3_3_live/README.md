# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 11:45:01 EDT`
Last processed slot: `early_entry_1145`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$18,164.25`
- Equity: `$32,504.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$240.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14340.0        35.25          35.85      477.34        476.76          bid_ask_mid                      35.85                bid_ask_mid                    True           240.0                    1.7         97.22               36              0.69         45.69           49.59                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           95.45               22            2.25              1.90        120.07                85.20         0.593          pass              0.587             15.8                           0.255                1.93              0.998                                 ok            True                  False
   TXN          100.00               14            1.88              4.17        314.16                35.59         0.522          pass              0.552             24.5                           0.425                0.59              0.475                                 ok            True                  False
  MDLZ           92.86               14            1.19              0.52         62.17                12.98         0.511          pass              0.568             49.0                           0.287                1.12              0.190                                 ok            True                  False
  SOXL           93.55               31            0.33              0.51        224.41               139.09         0.778          pass              0.841             87.3                           0.539               20.25              3.774                                 ok           False                  False
  INSM           72.22               36            1.01              0.76        108.04               111.11         0.770          pass              0.368             39.1                           0.445               -7.21             -0.375            downtrend_blocked_slope           False                  False
  MELI           95.24               42            0.11              1.29       1694.98                61.27         0.615          pass              0.926             88.1                           0.508                5.37              0.822                                 ok           False                  False
   AEP           77.78               18            0.39              0.35        127.61                25.60         0.590          pass              0.269             52.4                           0.427               -1.04              0.114                                 ok           False                  False
  REGN           87.88               33            0.59              2.58        620.41                44.05         0.552          pass              0.549             43.4                           0.276              -13.20             -1.066 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           90.00               10            1.86              5.09        387.95                41.30         0.544          pass              0.397             25.4                           0.361               -4.54             -0.337            downtrend_blocked_slope           False                  False
  SBUX          100.00                6            1.63              1.15        100.26                16.60         0.539          pass              0.598             47.9                           0.270               -6.31             -0.743            downtrend_blocked_slope           False                  False
   PEP           84.62               13            1.46              1.50        145.65                23.56         0.524          pass              0.261             22.0                           0.328               -3.04             -0.284            downtrend_blocked_slope           False                  False
  AMGN           89.66               29            0.44              1.04        336.03                27.03         0.520          pass              0.605             56.4                           0.430                0.38              0.275                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-29T11:45:01.211344-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:40:05.216205-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:35:06.186769-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:30:03.208249-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:25:01.209372-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:20:01.214678-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:15:06.204511-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:10:06.165530-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:05:07.175398-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:00:03.169868-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529114501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529114501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529114501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529114501)

</details>
