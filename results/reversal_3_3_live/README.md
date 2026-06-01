# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 11:05:05 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$16,749.25`
- Equity: `$31,869.25`
- Realized PnL: `$20,849.25`
- Unrealized PnL: `$1,020.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 15120.0        35.25           37.8      477.34         475.3          bid_ask_mid                       37.8                bid_ask_mid                    True          1020.0                   7.23         97.22               36              0.69         45.69           51.72                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  LRCX           88.00               25            1.56              3.46        316.70                55.15         0.546          pass              0.535             55.7                           0.563               10.01              1.557                                 ok            True                  False
  AAPL           92.31               13            1.58              3.45        310.58                17.18         0.520          pass              0.431             10.4                           0.202                2.30              0.455                                 ok            True                  False
  ISRG           82.35               17            1.88              5.58        422.25                37.20         0.516          pass              0.275             37.8                           0.335               -1.06             -0.424                                 ok            True                  False
  KLAC           91.43               35            0.77             10.31       1917.29                50.27         0.514          pass              0.699             58.8                           0.596                5.82              1.065                                 ok            True                  False
  INTC           95.65               23            2.50              2.01        113.82                88.16         0.506          pass              0.741             67.7                           0.852                2.80              0.656                                 ok            True                  False
  SOXL           93.55               31            0.41              0.64        224.07               138.67         0.769          pass              0.859             93.6                           0.824               36.09              4.522                                 ok           False                  False
  INSM           61.90               21            2.62              1.96        106.07               110.85         0.732          pass              0.156              3.1                           0.247               -4.61             -0.229                                 ok           False                  False
  ROST           88.89                9            1.90              3.08        230.41                40.27         0.605          pass              0.348             16.8                           0.139                6.85              1.018                                 ok           False                  False
  ASML           94.44               36            0.35              3.91       1611.09                52.38         0.579          pass              0.858             80.6                           0.722                7.02              0.978                                 ok           False                  False
   AEP           66.67                6            1.38              1.23        126.14                24.34         0.574          pass              0.100             14.2                           0.307               -0.18             -0.043                                 ok           False                  False
   WMT           76.92               13            1.39              1.13        115.27                32.67         0.562          pass              0.105              9.6                           0.163              -13.17             -1.687 downtrend_blocked_slope_and_streak           False                  False
  COST           71.43               14            1.08              7.20        953.23                27.93         0.543          pass              0.124             14.5                           0.199               -9.81             -1.324 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                            detail
2026-06-01T11:05:05.001730-04:00 early_entry_1105 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T11:00:06.868353-04:00 early_entry_1100 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:55:05.037823-04:00 early_entry_1055 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:50:02.030690-04:00 early_entry_1050 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:45:04.809408-04:00 early_entry_1045 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:40:02.889007-04:00 early_entry_1040 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:35:01.685578-04:00 early_entry_1035 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:30:02.004330-04:00 early_entry_1030 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:25:05.840855-04:00 early_entry_1025 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:25:05.840855-04:00      manage_1030          exit {"asset_type": "option", "contract_symbol": "MRVL260717C00200000", "fill_price": 25.47, "pnl": -1415.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MRVL"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601110505)

</details>
