# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 15:25:13 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$16,177.75`
- Equity: `$27,977.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$-340.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   0      4     12140.0                 11800.0        30.35           29.5      415.18        413.39          bid_ask_mid                       29.5                bid_ask_mid                    True          -340.0                   -2.8         91.67               36              0.62         50.17           50.17                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           97.14               35            0.66              0.55        118.72               113.85         0.732          pass              0.899             86.4                           0.739                7.80             -0.550                                 ok            True                   True
  FTNT          100.00               21            1.68              1.53        129.34                70.74         0.666          pass              0.602             20.7                           0.294               18.38              1.746                                 ok            True                  False
  PAYX           94.74               19            0.52              0.34         94.77                29.35         0.565          pass              0.741             77.3                           0.662                1.47              0.258                                 ok            True                  False
  MNST           84.85               33            0.67              0.41         86.71                49.77         0.539          pass              0.598             87.0                           0.740               13.60              0.670                                 ok            True                  False
   ADP           94.12               34            0.51              0.79        220.35                38.26         0.528          pass              0.806             72.1                           0.590                2.55              0.455                                 ok            True                   True
  NVDA           87.50               24            1.47              2.30        222.48                44.60         0.518          pass              0.467             40.6                           0.477                4.10              0.345                                 ok            True                  False
  ISRG           90.00               20            1.69              5.30        446.76                35.82         0.508          pass              0.520             45.4                           0.603               -2.65              0.015                                 ok            True                  False
  NXPI           78.57               14            3.21              6.96        307.17                91.65         0.661          pass              0.157             21.5                           0.306                3.44              0.195                                 ok           False                  False
  SBUX          100.00                7            1.88              1.41        105.90                31.64         0.606          pass              0.551             30.3                           0.435                0.81              0.168                                 ok           False                  False
  REGN           92.86               28            0.98              4.45        647.85                50.54         0.586          pass              0.630             36.2                           0.556               -9.13             -1.392 downtrend_blocked_slope_and_streak           False                  False
  MPWR           90.91               33            0.19              2.09       1552.37                57.81         0.567          pass              0.777             92.0                           0.841               -1.63             -0.712 downtrend_blocked_slope_and_streak           False                  False
  MSTR           90.00               40            0.40              0.47        165.61                64.80         0.552          pass              0.763             80.4                           0.451               -8.17             -1.499            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-05-21T15:10:07.725283-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-05-21T15:05:09.016170-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-05-21T15:00:06.517867-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-05-21T14:55:08.024423-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-05-21T14:50:05.768088-04:00       entry_1500  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T14:50:05.768088-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                         {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-21", "training_samples": 5058, "window": 5}
2026-05-21T12:00:02.068266-04:00 early_entry_1200  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T11:55:01.035616-04:00 early_entry_1155  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T11:50:01.038543-04:00 early_entry_1150          entry {"allocated_cash": 12140.0, "asset_type": "option", "contract_symbol": "AVGO260717C00420000", "contracts": 4, "early_entry_score": 0.724, "entry_mode": "early", "entry_option_price": 30.35, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2101.0, "option_spread_pct": 2.97, "option_volume": 296.0, "success_rate": 91.67, "ticker": "AVGO", "timing_score": 0.497}
2026-05-21T11:45:04.222670-04:00 early_entry_1145  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521152513)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521152513)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521152513)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521152513)

</details>
