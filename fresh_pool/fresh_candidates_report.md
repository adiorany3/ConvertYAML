# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-141MS` (url=279ms, nekobox=296ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-143MS` (url=306ms, nekobox=326ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-131MS` (url=276ms, nekobox=304ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-144MS` (url=288ms, nekobox=332ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-148MS` (url=285ms, nekobox=334ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-146MS` (url=297ms, nekobox=313ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-150MS` (url=303ms, nekobox=308ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-150MS` (url=336ms, nekobox=334ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-155MS` (url=293ms, nekobox=348ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-149MS` (url=280ms, nekobox=322ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-163MS` (url=284ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-153MS` (url=328ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-170MS` (url=307ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-163MS` (url=284ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-158MS` (url=325ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-176MS` (url=320ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-148MS` (url=420ms, status=HTTP 204)
18. `AKUN-018-DIXONS-VLESS-WS-166MS` (url=298ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-165MS` (url=320ms, status=HTTP 204)
20. `AKUN-020-UK-GB-DCL-01-20191003-VLESS-WS-204MS` (url=365ms, status=HTTP 204)
21. `AKUN-021-466688-VLESS-WS-186MS` (url=362ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-253MS` (url=470ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-236MS` (url=392ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-158MS` (url=309ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-358MS` (url=728ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
