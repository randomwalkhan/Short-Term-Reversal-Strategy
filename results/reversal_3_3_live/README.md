# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 10:10:01 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$14,483.50`
- Equity: `$29,283.50`
- Realized PnL: `$17,583.50`
- Unrealized PnL: `$1,700.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260618C00290000       2026-05-07                   1     10     13100.0                 14800.0         13.1           14.8      283.62        288.61          1700.0                  12.98         91.67               12              2.01         41.87           41.26                  67.07                1293.0          214.0               0.05                      ok
```

## Today's Closed Trades (2026-05-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  FAST           96.30               27            0.55              0.17         44.29                33.68         0.555            pass               -0.76             -0.064                                 ok            True
  ORLY           85.00               20            1.27              0.84         94.22                34.97         0.535            pass                0.26              0.221                                 ok            True
    ZS           80.95               21            2.68              2.87        151.56                60.77         0.504            pass                9.73              1.115                                 ok            True
  CHTR           85.19               27            1.62              1.81        159.46               119.32         0.781            pass              -12.48             -1.197            downtrend_blocked_slope           False
 CMCSA           85.71                7            1.77              0.32         26.10                61.43         0.707            pass               -6.47             -0.617 downtrend_blocked_slope_and_streak           False
  SHOP           86.36               22            2.73              2.13        110.83                82.33         0.591            pass              -13.62             -1.620 downtrend_blocked_slope_and_streak           False
  INSM           81.40               43            0.18              0.14        104.75                99.84         0.538            pass              -22.61             -1.979 downtrend_blocked_slope_and_streak           False
  NFLX           88.57               35            0.89              0.55         88.03                43.15         0.526            pass               -5.37             -0.609            downtrend_blocked_slope           False
  PYPL           94.59               37            0.40              0.13         46.16                42.03         0.524            pass               -8.81             -1.041 downtrend_blocked_slope_and_streak           False
  TEAM           62.50                8            6.11              3.95         90.68               115.49         0.520            pass               21.22              3.353                                 ok           False
  TMUS           87.18               39            0.40              0.54        193.97                36.72         0.505            pass                1.91              0.359                                 ok           False
  CRWD           90.91               44            0.05              0.17        505.66                48.11         0.498 below_threshold               12.80              1.153                                 ok           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-08T10:10:01.121937-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-08T10:05:06.101764-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-08T10:00:06.094621-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-08T09:55:06.107419-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-08T09:40:05.918205-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:35:06.024595-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:30:04.090136-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:25:02.109177-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T00:00:05.874567-04:00 data_refresh data_refresh                   {'saved': 92}
2026-05-07T16:10:04.394572-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508101001)

</details>
