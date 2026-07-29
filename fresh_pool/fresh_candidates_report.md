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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=202ms, nekobox=235ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-58MS` (url=197ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=198ms, nekobox=222ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=209ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-59MS` (url=207ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=201ms, nekobox=222ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS` (url=197ms, nekobox=235ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-66MS` (url=209ms, nekobox=225ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-68MS` (url=270ms, nekobox=249ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=204ms, nekobox=225ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-101MS` (url=218ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-82MS` (url=207ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-78MS` (url=204ms, status=HTTP 204)
14. `AKUN-014-EU-VLESS-WS-107MS` (url=202ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-118MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-124MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-RMGYVPN-VLESS-WS-133MS` (url=318ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-93MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-119MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-160MS` (url=347ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-163MS` (url=265ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-174MS` (url=206ms, status=HTTP 204)
23. `AKUN-023-LEVIKOGJGFDD-VLESS-WS-227MS` (url=492ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-129MS` (url=216ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-434MS` (url=755ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
