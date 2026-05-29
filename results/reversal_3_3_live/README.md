# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 11:35:06 EDT`
Last processed slot: `manage_1130`

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
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14340.0        35.25          35.85      477.34        474.91          bid_ask_mid                      35.85                bid_ask_mid                    True           240.0                    1.7         97.22               36              0.69         45.69            51.0                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           96.15               26            1.58              1.33        120.32                85.20         0.612            pass              0.691             41.0                           0.485                2.63              1.030                                 ok            True                  False
   TXN          100.00               14            1.81              4.00        314.23                35.59         0.527            pass              0.562             27.5                           0.440                0.67              0.478                                 ok            True                  False
  AMGN           88.89               27            0.54              1.27        335.94                27.03         0.526            pass              0.544             46.9                           0.330                0.29              0.270                                 ok            True                  False
  MDLZ           91.67               12            1.36              0.59         62.14                12.98         0.512            pass              0.500             41.4                           0.238                0.93              0.182                                 ok            True                  False
  INSM           70.59               34            1.12              0.85        108.01               111.11         0.773            pass              0.334             32.4                           0.336               -7.32             -0.380            downtrend_blocked_slope           False                  False
   AEP           75.00               16            0.47              0.42        127.58                25.60         0.595            pass              0.229             43.3                           0.310               -1.12              0.111                                 ok           False                  False
  MNST           95.65               46            0.07              0.04         87.97                49.61         0.559            pass              0.938             93.9                           0.527                2.46              0.191                                 ok           False                  False
  REGN           88.57               35            0.42              1.82        620.74                44.05         0.551            pass              0.631             60.1                           0.337              -13.05             -1.058 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.91               11            1.65              1.69        145.56                23.56         0.533            pass              0.386             11.8                           0.205               -3.23             -0.293            downtrend_blocked_slope           False                  False
 GOOGL           84.62               13            1.69              4.62        388.15                41.30         0.527            pass              0.293             32.3                           0.574               -4.37             -0.329            downtrend_blocked_slope           False                  False
  SBUX           90.00               10            1.53              1.08        100.29                16.60         0.504            pass              0.470             51.1                           0.284               -6.21             -0.738            downtrend_blocked_slope           False                  False
  GOOG           88.89               18            1.56              4.21        384.31                41.01         0.500 below_threshold              0.451             36.8                           0.594               -4.30             -0.338            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-29T11:35:06.186769-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:30:03.208249-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:25:01.209372-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:20:01.214678-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:15:06.204511-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:10:06.165530-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:05:07.175398-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:00:03.169868-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T10:55:06.987208-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T10:50:02.163774-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529113506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529113506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529113506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529113506)

</details>
