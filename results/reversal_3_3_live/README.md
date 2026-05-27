# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 13:45:05 EDT`
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

- Cash: `$19,575.25`
- Equity: `$31,095.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-490.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11520.0        60.05           57.6       531.8        524.15          bid_ask_mid                       57.6                bid_ask_mid                    True          -490.0                  -4.08         97.22               36              0.52         54.56           57.81                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.50               32            1.05              2.44        331.63                92.16         0.633          pass              0.534             41.5                           0.339               11.88              1.209                                 ok            True                  False
  INTC           94.44               18            3.63              3.14        122.18                91.80         0.576          pass              0.588             30.6                           0.435               -1.30              0.369                                 ok            True                  False
  ASML           88.89               27            1.97             22.56       1622.36                54.27         0.505          pass              0.504             34.3                           0.501                5.18              0.579                                 ok            True                  False
  MSFT           86.96               23            1.00              2.93        414.78                23.55         0.504          pass              0.428             35.1                           0.278                1.22              0.211                                 ok            True                  False
  INSM           67.86               28            1.83              1.40        108.27               110.60         0.726          pass              0.280             29.3                           0.449               -7.87             -0.883            downtrend_blocked_slope           False                  False
   AEP           66.67               12            0.90              0.83        130.55                25.21         0.594          pass              0.137             21.3                           0.211               -1.68              0.141                                 ok           False                  False
  FTNT          100.00                5            4.33              4.06        132.22                66.88         0.576          pass              0.539             27.1                           0.445               12.55              1.387                                 ok           False                  False
  GEHC           73.53               34            0.72              0.33         64.04                58.90         0.574          pass              0.353             45.3                           0.398                2.29              0.446                                 ok           False                  False
  REGN           88.89               36            0.45              2.01        633.76                48.91         0.573          pass              0.678             70.2                           0.640              -12.54             -1.475 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.83               24            0.27              0.18         94.72                30.13         0.572          pass              0.711             53.6                           0.345                2.18              0.587                                 ok           False                  False
  ORLY           70.59               17            1.48              0.93         89.47                38.82         0.543          pass              0.155             17.9                           0.325               -3.59             -0.015                                 ok           False                  False
  SBUX           96.97               33            0.18              0.13        101.37                33.52         0.535          pass              0.865             86.0                           0.371               -4.45             -0.462 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T12:00:02.710964-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:50:03.680135-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:45:03.631384-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:40:05.644907-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:35:01.763028-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:30:03.642153-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:25:02.657208-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:20:01.673157-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:15:01.657140-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527134505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527134505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527134505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527134505)

</details>
