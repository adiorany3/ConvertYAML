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
1. `AKUN-001-877774-VLESS-WS-58MS` (url=196ms, nekobox=225ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=221ms, nekobox=190ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS`
5. `AKUN-006-UNKNOWN-VLESS-WS-63MS` (url=206ms, nekobox=170ms, status=no)
6. `AKUN-004-HINET-NET-VLESS-WS-64MS`
7. `AKUN-005-UNKNOWN-VLESS-WS-73MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-68MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-89MS` (url=217ms, nekobox=175ms, status=no)
12. `AKUN-009-DIGITALOCEAN-VLESS-WS-81MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS`
14. `AKUN-015-LEVIKOGJGFDD-VLESS-WS-106MS` (url=201ms, status=HTTP 204)
15. `AKUN-016-1PASSWORD-VLESS-WS-64MS` (url=220ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-86MS` (url=205ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-73MS` (url=199ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-95MS` (url=198ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-84MS` (url=214ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-96MS` (url=210ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-83MS` (url=204ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-126MS` (url=201ms, status=HTTP 204)
23. `AKUN-024-RMGYVPN-VLESS-WS-139MS` (url=354ms, status=HTTP 204)
24. `AKUN-025-LEVIKOGJGFDD-VLESS-WS-58MS` (url=202ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-406MS` (url=697ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
