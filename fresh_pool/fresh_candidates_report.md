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
1. `AKUN-001-UNKNOWN-VLESS-WS-76MS` (url=230ms, nekobox=260ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-92MS` (url=230ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=230ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=229ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS` (url=231ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=206ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS` (url=207ms, nekobox=268ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=222ms, nekobox=255ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=209ms, nekobox=255ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=234ms, nekobox=295ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-123MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-131MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-92MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-SPEEDTEST-VLESS-WS-90MS` (url=199ms, status=HTTP 204)
15. `AKUN-015-ORG-VLESS-WS-91MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-116MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-OVH-VLESS-WS-77MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-146MS` (url=225ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-145MS` (url=216ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-115MS` (url=214ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-135MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-163MS` (url=258ms, status=HTTP 204)
23. `AKUN-023-PUBLICDOMAINREGISTRY-NET-VLESS-WS-105MS` (url=210ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-242MS` (url=344ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-253MS` (url=538ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
