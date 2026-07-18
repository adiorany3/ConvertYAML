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
1. `AKUN-001-UNKNOWN-VLESS-WS-122MS` (url=250ms, nekobox=288ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-130MS` (url=283ms, nekobox=309ms, status=yes)
3. `AKUN-003-WEBEX-VLESS-WS-132MS` (url=298ms, nekobox=293ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-133MS` (url=253ms, nekobox=327ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-134MS` (url=268ms, nekobox=285ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-134MS` (url=282ms, nekobox=293ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-134MS` (url=272ms, nekobox=287ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-141MS` (url=259ms, nekobox=292ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-141MS` (url=269ms, nekobox=302ms, status=yes)
10. `AKUN-010-UK-GB-DCL-01-20191003-VLESS-WS-149MS` (url=297ms, nekobox=306ms, status=yes)
11. `AKUN-011-US-VLESS-WS-135MS` (url=267ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-161MS` (url=358ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-143MS` (url=298ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-155MS` (url=289ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-144MS` (url=273ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-157MS` (url=264ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-133MS` (url=254ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-130MS` (url=268ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-150MS` (url=297ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-144MS` (url=276ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-164MS` (url=314ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-183MS` (url=301ms, status=HTTP 204)
23. `AKUN-023-ZVC-VLESS-WS-151MS` (url=283ms, status=HTTP 204)
24. `AKUN-024-CCWU-VLESS-WS-138MS` (url=268ms, status=HTTP 204)
25. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-362MS` (url=950ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
