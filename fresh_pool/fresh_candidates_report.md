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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=438ms, nekobox=320ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=331ms, nekobox=342ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-93MS` (url=299ms, nekobox=344ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=313ms, nekobox=316ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-119MS` (url=319ms, nekobox=325ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-121MS` (url=341ms, nekobox=327ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-130MS` (url=318ms, nekobox=354ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-126MS` (url=332ms, nekobox=351ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-129MS` (url=370ms, nekobox=328ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS` (url=302ms, nekobox=334ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-136MS` (url=312ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-138MS` (url=290ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-145MS` (url=310ms, status=HTTP 204)
14. `AKUN-014-VOV-VLESS-WS-164MS` (url=356ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-91MS` (url=311ms, status=HTTP 204)
16. `AKUN-016-US-VLESS-WS-146MS` (url=342ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-160MS` (url=330ms, status=HTTP 204)
18. `AKUN-018-466688-VLESS-WS-135MS` (url=390ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-97MS` (url=358ms, status=HTTP 204)
20. `AKUN-020-PUBLICDOMAINREGISTRY-NET-VLESS-WS-103MS` (url=346ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-132MS` (url=309ms, status=HTTP 204)
22. `AKUN-022-466688-VLESS-WS-170MS` (url=321ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-148MS` (url=339ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-303MS` (url=703ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-327MS` (url=611ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
