# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 13:35:03 EDT`
Last processed slot: `manage_1330`

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
- Equity: `$33,224.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$960.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 15060.0        35.25          37.65      477.34        477.64          bid_ask_mid                      37.65                bid_ask_mid                    True           960.0                   6.81         97.22               36              0.69         45.69           50.74                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           92.59               27            1.13              1.77        223.87               139.09         0.757          pass              0.693             56.1                           0.283               19.29              3.737                                 ok            True                  False
  INTC           95.45               22            2.32              1.96        120.05                85.20         0.589          pass              0.579             13.3                           0.173                1.86              0.995                                 ok            True                  False
   TXN          100.00               12            2.37              5.25        313.70                35.59         0.504          pass              0.484              6.8                           0.243                0.09              0.452                                 ok            True                  False
  INSM           72.97               37            0.76              0.57        108.12               111.11         0.778          pass              0.423             54.9                           0.455               -6.98             -0.363            downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.59              0.53        127.53                25.60         0.600          pass              0.163             27.6                           0.227               -1.24              0.105                                 ok           False                  False
  REGN           86.21               29            0.87              3.78        619.90                44.05         0.559          pass              0.399             17.1                           0.150              -13.44             -1.079 downtrend_blocked_slope_and_streak           False                  False
  AMAT           91.43               35            0.22              0.71        449.38                50.48         0.556          pass              0.751             74.6                           0.377                1.97              0.641                                 ok           False                  False
  KLAC           91.43               35            0.40              5.41       1925.31                52.36         0.540          pass              0.632             35.5                           0.277                1.55              0.902                                 ok           False                  False
 GOOGL           90.00               10            1.95              5.31        387.85                41.30         0.539          pass              0.387             22.2                           0.288               -4.62             -0.341            downtrend_blocked_slope           False                  False
  GOOG           90.91               11            1.77              4.79        384.07                41.01         0.538          pass              0.436             28.2                           0.327               -4.50             -0.348            downtrend_blocked_slope           False                  False
  SBUX          100.00                6            1.72              1.21        100.23                16.60         0.533          pass              0.589             45.1                           0.449               -6.39             -0.747            downtrend_blocked_slope           False                  False
  AMGN           90.00               30            0.39              0.92        336.09                27.03         0.517          pass              0.637             61.7                           0.426                0.44              0.277                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-29T12:00:03.057178-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:55:04.089378-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:50:02.199680-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:45:01.211344-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:40:05.216205-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:35:06.186769-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:30:03.208249-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:25:01.209372-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:20:01.214678-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:15:06.204511-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529133503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529133503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529133503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529133503)

</details>
