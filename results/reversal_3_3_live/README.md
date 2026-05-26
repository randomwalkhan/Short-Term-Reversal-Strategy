# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 11:55:03 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$31,585.25`
- Equity: `$31,585.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26       30.350     36.1500  2320.0   19.110379 take_profit_day2_hit_at_scan
  SBUX     option         option SBUX260717C00105000     38          2026-05-22         2026-05-26        3.625      3.2625 -1377.5  -10.000000        stop_loss_hit_at_scan
  TTWO     option         option TTWO260717C00230000     15          2026-05-26         2026-05-26        9.800     11.3500  2325.0   15.816327 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           90.48               42            0.84              0.50         85.21               109.49         0.672          pass              0.784             79.1                           0.633               -2.98              0.041                                 ok            True                   True
  MELI           92.31               26            1.31             15.29       1657.87                60.80         0.600          pass              0.658             54.5                           0.622                5.48              0.706                                 ok            True                  False
   ADP           93.33               15            1.94              3.06        224.00                37.70         0.546          pass              0.512             22.9                           0.514                4.38              0.660                                 ok            True                  False
  PAYX           92.31               13            1.21              0.82         96.65                28.52         0.545          pass              0.582             59.8                           0.669                3.39              0.601                                 ok            True                  False
  ASML           86.21               29            1.60             18.26       1625.08                54.77         0.542          pass              0.346              0.0                           0.150                2.62              0.328                                 ok            True                  False
  CTSH           89.29               28            1.06              0.39         52.58                46.65         0.524          pass              0.618             66.1                           0.683                6.72              1.342                                 ok            True                  False
   ROP           88.24               17            1.76              4.03        325.21                26.18         0.506          pass              0.360             14.3                           0.338               -2.32              0.045                                 ok            True                  False
  CSCO           83.33                6            2.06              1.74        119.67                52.25         0.649          pass              0.229             25.2                           0.411               19.46              1.874                                 ok           False                  False
  INTU           78.57               14            3.51              7.86        316.57                90.56         0.635          pass              0.131             13.6                           0.381              -21.50             -2.278            downtrend_blocked_slope           False                  False
   TRI           73.33               15            1.28              0.77         85.53                55.00         0.626          pass              0.252             52.2                           0.463               -4.28              0.108                                 ok           False                  False
  SBUX           93.33               15            1.09              0.78        102.77                33.02         0.604          pass              0.603             51.4                           0.535               -2.98             -0.259            downtrend_blocked_slope           False                  False
   WMT           94.12               17            1.08              0.91        119.88                34.37         0.590          pass              0.568             28.6                           0.373               -6.76             -0.833 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-26T11:55:03.347264-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:50:02.331992-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:45:01.347976-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:40:05.359008-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:35:01.343425-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:30:01.341956-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:25:01.332906-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:20:01.352478-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:15:02.326421-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-26T11:10:05.334078-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526115503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526115503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526115503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526115503)

</details>
