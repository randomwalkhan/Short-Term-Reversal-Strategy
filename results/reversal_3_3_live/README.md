# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 14:15:04 EDT`
Last processed slot: `manual`

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
- Equity: `$32,964.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$700.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14800.0        35.25           37.0      477.34        475.88          bid_ask_mid                       37.0                bid_ask_mid                    True           700.0                   4.96         97.22               36              0.69         45.69           52.18                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           92.31               26            1.50              2.35        223.62               139.09         0.741          pass              0.643             44.6                           0.473               18.84              3.720                                 ok            True                  False
  INTC           95.24               21            2.90              2.45        119.84                85.20         0.548          pass              0.569             13.7                           0.334                1.26              0.968                                 ok            True                  False
  INSM           69.70               33            1.25              0.95        107.96               111.11         0.770          pass              0.306             25.3                           0.219               -7.45             -0.386            downtrend_blocked_slope           False                  False
  MELI           94.87               39            0.32              3.78       1693.91                61.27         0.620          pass              0.848             65.2                           0.312                5.15              0.812                                 ok           False                  False
   AEP           69.23               13            0.67              0.59        127.51                25.60         0.595          pass              0.137             19.0                           0.260               -1.31              0.102                                 ok           False                  False
  AMAT           91.43               35            0.08              0.27        449.57                50.48         0.566          pass              0.799             90.5                           0.574                2.11              0.647                                 ok           False                  False
  REGN           84.62               26            1.11              4.83        619.45                44.05         0.559          pass              0.306              6.6                           0.173              -13.65             -1.090 downtrend_blocked_slope_and_streak           False                  False
  KLAC           91.67               36            0.13              1.74       1926.89                52.36         0.549          pass              0.793             84.7                           0.587                1.83              0.914                                 ok           False                  False
 GOOGL           90.00               10            1.94              5.29        387.86                41.30         0.539          pass              0.388             22.6                           0.344               -4.61             -0.341            downtrend_blocked_slope           False                  False
  GOOG           90.91               11            1.78              4.80        384.06                41.01         0.537          pass              0.435             28.0                           0.369               -4.51             -0.348            downtrend_blocked_slope           False                  False
  SBUX          100.00                6            1.91              1.34        100.17                16.60         0.521          pass              0.569             39.0                           0.296               -6.57             -0.755            downtrend_blocked_slope           False                  False
  AMGN           90.62               32            0.30              0.71        336.18                27.03         0.509          pass              0.692             70.3                           0.666                0.53              0.281                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529141504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529141504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529141504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529141504)

</details>
