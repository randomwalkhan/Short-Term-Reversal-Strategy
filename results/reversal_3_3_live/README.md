# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 08:10:06 EDT`
Last processed slot: `share_ext_0810`

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

- Cash: `$2,402.75`
- Equity: `$28,552.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$235.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SBUX     option         option SBUX260717C00105000       2026-05-22                   1     38     13775.0                 14250.0         3.62           3.75      103.16        103.20     last_price_stale                        NaN                unavailable                   False           475.0                   3.45         94.74               19              0.93         28.13            1.56                  32.97                2147.0           78.0               0.07                      ok
  AVGO     option         option AVGO260717C00420000       2026-05-21                   2      4     12140.0                 11900.0        30.35          29.75      415.18        416.99     last_price_stale                        NaN                unavailable                   False          -240.0                  -1.98         91.67               36              0.62         50.17            0.78                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-26)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et           slot    event_type                                                     detail
2026-05-26T00:00:03.086607-04:00   data_refresh  data_refresh                                              {'saved': 92}
2026-05-25T23:55:01.101287-04:00 share_ext_2355 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:50:02.099383-04:00 share_ext_2350 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:45:01.097228-04:00 share_ext_2345 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:40:05.102217-04:00 share_ext_2340 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:35:01.093781-04:00 share_ext_2335 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:30:01.103317-04:00 share_ext_2330 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:25:02.099760-04:00 share_ext_2325 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:20:01.104241-04:00 share_ext_2320 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:15:05.147623-04:00 share_ext_2315 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526081006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526081006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526081006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526081006)

</details>
