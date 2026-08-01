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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=207ms, nekobox=172ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS`
3. `AKUN-002-UNKNOWN-VLESS-WS-64MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS`
5. `AKUN-004-ALIBABA-VLESS-WS-58MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS` (url=213ms, nekobox=182ms, status=no)
8. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-66MS` (url=219ms, nekobox=185ms, status=no)
10. `AKUN-007-CLOUDFLARE-VLESS-WS-67MS`
11. `AKUN-008-UNKNOWN-VLESS-WS-65MS`
12. `AKUN-009-UNKNOWN-VLESS-WS-65MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-61MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-72MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-DIGITALOCEAN-VLESS-WS-68MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-124MS` (url=315ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-101MS` (url=201ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-104MS` (url=211ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-109MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-CHATGPT-VLESS-WS-80MS` (url=202ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-145MS` (url=217ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-103MS` (url=200ms, status=HTTP 204)
23. `AKUN-023-LEVIKOGJGFDD-VLESS-WS-93MS` (url=204ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-75MS` (url=201ms, status=HTTP 204)
25. `AKUN-026-SUKARIO-VLESS-WS-384MS` (url=646ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
