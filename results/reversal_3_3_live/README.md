# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 09:30:01 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$17,648.00`
- Equity: `$31,448.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$375.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX260918C00310000       2026-08-10                   2      5     13425.0                 13800.0        26.85           27.6      307.66        326.73     last_price_stale                        NaN                unavailable                   False           375.0                   2.79          87.1               31              1.19         68.92             0.0                  90.05                1499.0           93.0               0.03                      ok
```

## Today's Closed Trades (2026-08-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           89.47               19            1.34              0.55         58.76                59.96         0.687          pass              0.506             41.5                           0.352               -0.19              0.183                  ok            True                  False
 CMCSA           90.48               21            0.51              0.09         25.61                42.20         0.650          pass              0.540             40.9                           0.332                3.70              0.662                  ok            True                  False
  GEHC           94.44               18            1.86              0.94         72.35                58.44         0.627          pass              0.501              0.0                           0.198               11.37              0.679                  ok            True                  False
  ABNB          100.00               10            2.77              3.59        183.44                63.49         0.620          pass              0.478              5.4                           0.155               17.46              1.859                  ok            True                  False
   ROP          100.00               10            2.41              6.73        396.62                43.71         0.612          pass              0.467              2.0                           0.263               -4.46              0.023                  ok            True                  False
  DXCM           85.71               28            1.01              0.63         89.26                59.86         0.605          pass              0.526             64.3                           0.440               17.95              1.455                  ok            True                  False
  PAYX          100.00               15            1.09              0.92        120.90                32.99         0.603          pass              0.500              2.2                           0.190               -1.76              0.218                  ok            True                  False
   ADP           96.43               28            0.90              1.70        270.36                32.38         0.539          pass              0.696             40.6                           0.270               -1.72              0.112                  ok            True                  False
  WDAY           88.00               25            2.89              3.66        179.70                70.31         0.520          pass              0.404             13.0                           0.222                4.78              1.113                  ok            True                  False
  REGN           90.00               30            0.97              5.44        794.67                33.07         0.509          pass              0.451              0.0                           0.257               13.49              1.084                  ok            True                  False
   PEP           82.76               29            0.52              0.50        138.19                20.85         0.508          pass              0.347             32.2                           0.346               -1.79             -0.179                  ok            True                  False
  IDXX           93.75               16            1.74              7.15        583.57                28.76         0.502          pass              0.457              0.0                           0.261                1.17              0.465                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-08-12T09:30:01.771593-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:25:01.593760-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:20:03.729351-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:15:01.696450-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:10:04.748220-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:05:02.776077-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:00:03.695691-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T08:55:02.907270-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T08:50:06.776266-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T08:45:01.795607-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812093001)

</details>
