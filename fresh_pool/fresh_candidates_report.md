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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-133MS` (url=271ms, nekobox=294ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-134MS` (url=274ms, nekobox=294ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-137MS` (url=254ms, nekobox=297ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-139MS` (url=266ms, nekobox=299ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-152MS` (url=263ms, nekobox=301ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-142MS` (url=267ms, nekobox=289ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-144MS` (url=285ms, nekobox=294ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-155MS` (url=272ms, nekobox=308ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-160MS` (url=308ms, nekobox=302ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-150MS` (url=266ms, nekobox=288ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-142MS` (url=273ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-142MS` (url=267ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-170MS` (url=270ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-170MS` (url=344ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-161MS` (url=285ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-158MS` (url=266ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-150MS` (url=262ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-151MS` (url=277ms, status=HTTP 204)
19. `AKUN-019-POLICE-VLESS-WS-157MS` (url=309ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-161MS` (url=324ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-144MS` (url=273ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-222MS` (url=313ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-206MS` (url=316ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-183MS` (url=338ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-161MS` (url=350ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
