# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 11:20:01 EDT`
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
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14340.0        35.25          35.85      477.34        474.55          bid_ask_mid                      35.85                bid_ask_mid                    True           240.0                    1.7         97.22               36              0.69         45.69           51.22                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           95.65               23            1.94              1.65        120.18                85.20         0.607          pass              0.629             27.2                           0.299                2.25              1.013                                 ok            True                  False
   TXN          100.00               13            2.22              4.90        313.85                35.59         0.508          pass              0.504             11.2                           0.155                0.25              0.459                                 ok            True                  False
  SOXL           93.55               31            0.34              0.53        224.40               139.09         0.777          pass              0.839             86.8                           0.521               20.24              3.773                                 ok           False                  False
  INSM           72.22               36            1.08              0.82        108.02               111.11         0.766          pass              0.354             34.6                           0.344               -7.28             -0.378            downtrend_blocked_slope           False                  False
   AEP           76.47               17            0.41              0.36        127.60                25.60         0.594          pass              0.257             50.5                           0.315               -1.06              0.114                                 ok           False                  False
  MNST           95.65               46            0.05              0.03         87.98                49.61         0.560          pass              0.942             95.5                           0.489                2.48              0.191                                 ok           False                  False
  REGN           88.57               35            0.45              1.97        620.67                44.05         0.548          pass              0.620             56.7                           0.266              -13.08             -1.060 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           90.00               10            1.94              5.30        387.86                41.30         0.539          pass              0.387             22.3                           0.426               -4.62             -0.341            downtrend_blocked_slope           False                  False
   PEP           91.67               12            1.50              1.54        145.63                23.56         0.538          pass              0.432             17.9                           0.161               -3.08             -0.286            downtrend_blocked_slope           False                  False
  GOOG           90.91               11            1.79              4.85        384.04                41.01         0.536          pass              0.433             27.3                           0.450               -4.53             -0.349            downtrend_blocked_slope           False                  False
  AMGN           90.00               30            0.41              0.97        336.07                27.03         0.515          pass              0.630             59.6                           0.419                0.42              0.276                                 ok           False                  False
  SBUX           90.91               11            1.30              0.91        100.36                16.60         0.514          pass              0.525             58.6                           0.307               -5.99             -0.727            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-29T11:20:01.214678-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:15:06.204511-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:10:06.165530-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:05:07.175398-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:00:03.169868-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T10:55:06.987208-04:00 early_entry_1055 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T10:50:02.163774-04:00 early_entry_1050 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T10:45:04.066585-04:00 early_entry_1045 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T10:40:02.188936-04:00 early_entry_1040 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T10:35:01.212926-04:00 early_entry_1035 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529112001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529112001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529112001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529112001)

</details>
