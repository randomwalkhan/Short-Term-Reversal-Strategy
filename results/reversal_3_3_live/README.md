# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 10:25:06 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$73,431.80`
- Equity: `$141,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-3,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 68400.0        17.85           17.1      223.97        221.96          bid_ask_mid                       17.1                bid_ask_mid                    True         -3000.0                   -4.2         100.0               38              0.68         80.16           82.39                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           84.62               13            1.83              0.32         24.95                34.71         0.539          pass              0.197              0.0                           0.008               10.60              1.073                                 ok            True                  False
   WMT           81.25               16            1.02              0.87        120.75                23.20         0.534          pass              0.151              8.1                           0.094                7.66              0.749                                 ok            True                  False
  TEAM          100.00               39            0.54              0.84        222.80                49.30         0.532          pass              0.833             62.2                           0.380                7.34              0.933                                 ok            True                  False
   EXC           80.00               15            1.04              0.33         44.71                20.91         0.529          pass              0.168             27.3                           0.211                6.29              0.568                                 ok            True                  False
   MAR           87.50               16            1.26              3.49        395.30                21.06         0.523          pass              0.342             16.4                           0.183                7.09              0.933                                 ok            True                  False
   ADP           90.00               20            0.94              2.02        307.08                23.94         0.516          pass              0.563             59.2                           0.335               12.62              1.229                                 ok            True                  False
  ORLY          100.00               15            1.46              0.94         91.60                17.78         0.513          pass              0.485              0.0                           0.158                4.87              0.607                                 ok            True                  False
   AEP           85.00               20            0.83              0.76        130.31                17.81         0.513          pass              0.261              3.1                           0.083                5.49              0.482                                 ok            True                  False
  GILD           90.00               30            0.72              0.79        156.85                28.18         0.502          pass              0.499             16.3                           0.249                3.23              0.416                                 ok            True                  False
   CEG           87.88               33            0.84              1.49        254.57                65.49         0.594          pass              0.642             73.2                           0.792              -15.10             -1.678 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                1            2.45              1.12         64.71                24.03         0.563          pass              0.461              1.5                           0.143                5.27              0.528                                 ok           False                  False
  REGN           77.78                9            1.98             11.34        814.23                31.70         0.550          pass              0.060              1.6                           0.170                7.55              0.824                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-23T10:25:06.029286-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:20:06.283023-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:15:04.978635-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:10:06.503805-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:05:04.082507-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:00:04.565947-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T00:00:06.660227-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-22T15:10:06.169647-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-22T15:05:02.793544-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-22T15:00:05.670192-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023102506)

</details>
