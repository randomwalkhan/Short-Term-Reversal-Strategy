# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 10:50:01 EDT`
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

- Cash: `$19,575.25`
- Equity: `$31,735.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$150.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 12160.0        60.05           60.8       531.8        529.29          bid_ask_mid                       60.8                bid_ask_mid                    True           150.0                   1.25         97.22               36              0.52         54.56           57.99                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.88               33            0.84              1.95        331.83                92.16         0.640          pass              0.587             53.1                           0.508               12.12              1.219                                 ok            True                  False
  INTC           95.65               23            2.69              2.32        122.52                91.80         0.605          pass              0.693             48.6                           0.718               -0.34              0.414                                 ok            True                  False
  ISRG           90.91               11            2.51              7.68        433.35                35.34         0.528          pass              0.354              1.0                           0.084               -1.44              0.132                                 ok            True                  False
  ASML           89.29               28            1.74             19.90       1623.50                54.27         0.514          pass              0.545             42.0                           0.509                5.43              0.590                                 ok            True                  False
  ORLY           83.33               30            1.09              0.69         89.58                38.82         0.502          pass              0.298              8.4                           0.217               -3.21              0.003                                 ok            True                  False
  INSM           69.70               33            1.40              1.07        108.41               110.60         0.733          pass              0.265             12.7                           0.124               -7.46             -0.863            downtrend_blocked_slope           False                  False
   AEP           66.67               12            0.74              0.68        130.61                25.21         0.604          pass              0.180             35.3                           0.267               -1.52              0.148                                 ok           False                  False
  REGN           83.33               24            1.33              5.90        632.09                48.91         0.588          pass              0.278             12.4                           0.155              -13.31             -1.515 downtrend_blocked_slope_and_streak           False                  False
  FTNT          100.00                6            4.19              3.93        132.28                66.88         0.578          pass              0.546             29.5                           0.393               12.72              1.394                                 ok           False                  False
  GEHC           78.57               42            0.11              0.05         64.16                58.90         0.576          pass              0.505             82.5                           0.375                2.92              0.474                                 ok           False                  False
  ROST           94.29               35            0.49              0.81        234.33                38.50         0.525          pass              0.809             69.5                           0.545                7.28              1.022                                 ok           False                  False
  UPRO           94.59               37            0.14              0.15        145.80                30.88         0.512          pass              0.835             71.6                           0.447                4.39              0.292                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-27T10:50:01.641792-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:45:02.652833-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:40:01.617422-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:35:01.630649-04:00 early_entry_1035         entry {"allocated_cash": 12010.0, "asset_type": "option", "contract_symbol": "SNPS260717C00500000", "contracts": 2, "early_entry_score": 0.805, "entry_mode": "early", "entry_option_price": 60.05, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 302.0, "option_spread_pct": 9.83, "option_volume": 157.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.413}
2026-05-27T10:30:06.423656-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:25:01.625508-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:20:05.595233-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:15:02.626707-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:10:01.607453-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:05:01.657651-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527105001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527105001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527105001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527105001)

</details>
