# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=222ms, nekobox=228ms, status=yes)
2. `AKUN-002-WPENG-VLESS-WS-73MS` (url=238ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=237ms, nekobox=254ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-62MS` (url=218ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=218ms, nekobox=237ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-93MS` (url=215ms, nekobox=252ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-101MS` (url=227ms, nekobox=252ms, status=yes)
8. `AKUN-008-466688-VLESS-WS-83MS` (url=228ms, nekobox=259ms, status=yes)
9. `AKUN-009-PUBLICDOMAINREGISTRY-NET-VLESS-WS-108MS` (url=225ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS` (url=225ms, nekobox=255ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-111MS` (url=201ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-102MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-97MS` (url=231ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-129MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-98MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-229MS` (url=502ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-258MS` (url=507ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-269MS` (url=564ms, status=HTTP 204)
19. `AKUN-024-CELESTARA-VLESS-WS-379MS` (url=586ms, status=HTTP 204)
20. `AKUN-029-UNKNOWN-VLESS-WS-289MS` (url=528ms, status=HTTP 204)
21. `AKUN-032-UNKNOWN-VLESS-WS-529MS` (url=796ms, status=HTTP 204)
22. `AKUN-033-CLOUDFLARE-VLESS-WS-530MS` (url=973ms, status=HTTP 204)
23. `AKUN-034-UNKNOWN-VLESS-WS-616MS` (url=767ms, status=HTTP 204)
24. `AKUN-035-DEV-VLESS-WS-756MS` (url=853ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
