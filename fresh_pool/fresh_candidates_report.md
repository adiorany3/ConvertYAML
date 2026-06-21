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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=231ms, nekobox=258ms, status=yes)
2. `AKUN-002-104-253-175-0-1-VLESS-WS-65MS` (url=256ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=224ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=233ms, nekobox=261ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=285ms, nekobox=266ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=228ms, nekobox=259ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-83MS` (url=235ms, nekobox=274ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=249ms, nekobox=180ms, status=no)
9. `AKUN-008-VULTR-VLESS-WS-68MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-78MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS`
12. `AKUN-012-VULTR-VLESS-WS-98MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-121MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-120MS` (url=243ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-76MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-130MS` (url=229ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-294MS` (url=651ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-272MS` (url=543ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-252MS` (url=563ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-269MS` (url=570ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-318MS` (url=678ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-91MS` (url=258ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-281MS` (url=581ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-171MS` (url=680ms, status=HTTP 204)
25. `AKUN-028-GROK-VLESS-WS-404MS` (url=522ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
