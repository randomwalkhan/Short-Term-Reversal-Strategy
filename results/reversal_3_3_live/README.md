# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 10:05:06 EDT`
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
   TXN     option         option TXN260618C00290000       2026-05-07                   1     10     13100.0                 14800.0         13.1           14.8      283.62        289.48          1700.0                  12.98         91.67               12              2.01         41.87           40.47                  67.07                1293.0          214.0               0.05                      ok
```

## Today's Closed Trades (2026-05-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
   ADP           85.71               14            2.01              3.01        212.80                38.09         0.509            pass                6.74              0.662                                 ok            True
  CHTR           81.82               22            2.02              2.27        159.27               119.32         0.782            pass              -12.84             -1.216            downtrend_blocked_slope           False
 CMCSA           88.89                9            1.49              0.27         26.12                61.43         0.717            pass               -6.21             -0.604 downtrend_blocked_slope_and_streak           False
  SHOP           85.71               21            2.90              2.27        110.77                82.33         0.586            pass              -13.78             -1.628 downtrend_blocked_slope_and_streak           False
  NFLX           90.32               31            1.03              0.64         87.99                43.15         0.545            pass               -5.50             -0.615            downtrend_blocked_slope           False
  PYPL           92.86               28            0.91              0.29         46.09                42.03         0.539            pass               -9.27             -1.065 downtrend_blocked_slope_and_streak           False
  FAST           97.30               37            0.11              0.03         44.35                33.68         0.524            pass               -0.32             -0.044                                 ok           False
  TEAM           71.43                7            6.40              4.14         90.60               115.49         0.523            pass               20.84              3.339                                 ok           False
  CDNS           97.67               43            0.04              0.11        356.85                51.38         0.522            pass                7.16              0.945                                 ok           False
  TMUS           88.10               42            0.16              0.22        194.11                36.72         0.503            pass                2.15              0.370                                 ok           False
  CRWD           90.24               41            0.44              1.56        505.07                48.11         0.492 below_threshold               12.36              1.136                                 ok           False
    ZS           78.95               19            3.18              3.40        151.33                60.77         0.485 below_threshold                9.18              1.092                                 ok           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-05-08T10:05:06.101764-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-08T10:00:06.094621-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-08T09:55:06.107419-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-05-08T09:40:05.918205-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:35:06.024595-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:30:04.090136-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T09:25:02.109177-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-05-08T00:00:05.874567-04:00 data_refresh data_refresh                   {'saved': 92}
2026-05-07T16:10:04.394572-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-05-07T16:05:04.301944-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508100506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508100506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508100506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508100506)

</details>
