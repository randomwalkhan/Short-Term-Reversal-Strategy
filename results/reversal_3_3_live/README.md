# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 09:55:01 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$50,178.10`
- Equity: `$50,178.10`
- Realized PnL: `$40,178.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-31)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00155000     29          2026-08-28         2026-08-31          9.0         8.1 -2610.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MNST           83.33               12            1.52              0.50         46.65               551.82         1.000          pass              0.262             20.0                           0.165                1.38              0.010                  ok            True                  False
  ABNB          100.00               14            1.86              2.47        188.37                62.79         0.690          pass              0.529             11.0                           0.213                3.69              0.301                  ok            True                  False
  MELI          100.00               14            1.95             26.78       1954.77                48.83         0.622          pass              0.527             12.8                           0.193                7.86              0.800                  ok            True                  False
   TRI           92.00               25            1.54              1.14        105.73                60.45         0.590          pass              0.683             67.9                           0.496                6.27              0.414                  ok            True                  False
  AMGN          100.00               20            0.74              2.25        431.46                27.94         0.580          pass              0.675             50.0                           0.502                2.94              0.240                  ok            True                  False
  PAYX          100.00               22            0.84              0.75        126.72                24.67         0.556          pass              0.615             26.6                           0.253                6.27              0.606                  ok            True                  False
  VRTX           96.55               29            0.86              3.25        540.30                33.03         0.543          pass              0.734             50.9                           0.506                4.17              0.287                  ok            True                  False
   KDP           82.61               23            1.21              0.27         32.06                30.92         0.527          pass              0.230              7.1                           0.075                4.99              0.478                  ok            True                  False
  SBUX           96.00               25            0.52              0.39        107.68                22.68         0.525          pass              0.715             54.1                           0.462               -0.58              0.160                  ok            True                  False
   MAR           92.31               13            1.71              4.19        349.28                33.77         0.522          pass              0.476             25.3                           0.243               -3.02             -0.223                  ok            True                  False
 CMCSA           90.00               20            1.22              0.23         26.96                25.33         0.520          pass              0.406              7.0                           0.193                4.54              0.362                  ok            True                  False
  CTAS           85.00               20            0.87              1.24        203.65                14.76         0.519          pass              0.294             14.1                           0.261                2.32              0.228                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                                                                                                                                          detail
2026-08-31T09:50:01.420574-04:00    manage_1000          exit {"asset_type": "option", "contract_symbol": "SHOP261016C00155000", "fill_price": 8.1, "pnl": -2610.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-08-31T03:00:02.021557-04:00   data_refresh  data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-29T02:55:05.202083-04:00 share_ext_0255 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:50:05.132580-04:00 share_ext_0250 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:45:01.295429-04:00 share_ext_0245 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:40:01.326395-04:00 share_ext_0240 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:35:05.989284-04:00 share_ext_0235 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:30:05.313779-04:00 share_ext_0230 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:25:01.129841-04:00 share_ext_0225 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:20:04.124730-04:00 share_ext_0220 market_closed                                                                                                                                     {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831095501)

</details>
