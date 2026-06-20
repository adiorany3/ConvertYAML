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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-81MS` (url=232ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-96MS` (url=232ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-97MS` (url=206ms, nekobox=237ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-116MS` (url=237ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-118MS` (url=227ms, nekobox=196ms, status=no)
6. `AKUN-005-UNKNOWN-VLESS-WS-115MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-148MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-152MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-161MS` (url=203ms, nekobox=203ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-258MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-253MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-269MS` (url=641ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-108MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-278MS` (url=593ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-288MS` (url=592ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-292MS` (url=586ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-249MS` (url=534ms, status=HTTP 204)
19. `AKUN-021-GROK-VLESS-WS-87MS` (url=472ms, status=HTTP 204)
20. `AKUN-027-UNKNOWN-VLESS-WS-453MS` (url=566ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-393MS` (url=566ms, status=HTTP 204)
22. `AKUN-029-CLOUDFLARE-VLESS-WS-461MS` (url=698ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-542MS` (url=1417ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-584MS` (url=887ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
