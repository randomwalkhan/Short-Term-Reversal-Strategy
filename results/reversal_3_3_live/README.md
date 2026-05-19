# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 11:15:01 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$14,090.00`
- Equity: `$27,837.50`
- Realized PnL: `$17,837.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PANW     option         option PANW260618C00250000       2026-05-19                   0      9     13747.5                 13747.5        15.28          15.28      245.93        246.39          bid_ask_mid                      15.28                bid_ask_mid                    True             0.0                    0.0         91.67               36              0.66         58.04           59.07                  42.55                2852.0           34.0                0.1                      ok
```

## Today's Closed Trades (2026-05-19)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TTWO     option         option TTWO260618C00250000     10          2026-05-18         2026-05-19        13.55      12.195 -1355.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           92.59               27            0.77              1.62        299.90                69.24         0.670          pass              0.750             78.0                           0.736                6.15              0.721                                 ok            True                  False
  GOOG           80.00               10            1.92              5.29        390.84                40.55         0.571          pass              0.107             16.7                           0.237                0.34              0.012                                 ok            True                  False
 GOOGL           80.00               10            2.03              5.65        394.52                40.53         0.568          pass              0.094             12.3                           0.215                0.11              0.020                                 ok            True                  False
  ASML           83.33               30            0.97             10.01       1468.10                50.95         0.537          pass              0.438             54.0                           0.693                1.05             -0.153                                 ok            True                  False
  SNPS           97.14               35            0.81              2.82        497.22                41.65         0.527          pass              0.765             48.6                           0.492               -1.61             -0.168                                 ok            True                  False
  FAST           91.30               23            1.00              0.31         43.87                22.17         0.507          pass              0.578             46.3                           0.573               -1.74             -0.204                                 ok            True                  False
  AVGO           85.71               14            2.70              7.94        417.31                42.85         0.504          pass              0.300             23.6                           0.356               -4.21             -0.138                                 ok            True                  False
  INTC          100.00               21            2.22              1.68        107.45               114.00         0.707          pass              0.719             58.3                           0.775               -2.21             -0.484 downtrend_blocked_slope_and_streak           False                  False
  TEAM           91.30               46            0.26              0.16         89.36               113.67         0.693          pass              0.786             71.8                           0.451               -3.41             -0.580           downtrend_blocked_streak           False                  False
  QCOM          100.00                2            4.55              6.49        200.86                99.05         0.637          pass              0.543             26.5                           0.512                4.19              0.112                                 ok           False                  False
  MNST           66.67                9            2.41              1.49         87.90                49.83         0.593          pass              0.078              6.2                           0.186               14.00              1.451                                 ok           False                  False
  CSCO           80.00                5            2.81              2.34        117.88                49.96         0.591          pass              0.114             18.3                           0.379               22.52              2.903                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                             detail
2026-05-19T11:15:01.967392-04:00 early_entry_1115 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:10:06.161691-04:00 early_entry_1110 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:05:01.947940-04:00 early_entry_1105 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:00:04.023655-04:00 early_entry_1100 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T11:00:04.023655-04:00      manage_1100          exit {"asset_type": "option", "contract_symbol": "TTWO260618C00250000", "fill_price": 12.195, "pnl": -1355.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TTWO"}
2026-05-19T10:55:01.036439-04:00 early_entry_1055 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T10:50:05.059636-04:00 early_entry_1050 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T10:45:01.038335-04:00 early_entry_1045 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T10:40:01.036176-04:00 early_entry_1040 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-19T10:35:03.933477-04:00 early_entry_1035 entry_skipped                                                                                                                                                    {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519111501)

</details>
