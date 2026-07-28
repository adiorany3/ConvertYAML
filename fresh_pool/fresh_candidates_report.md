# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=228ms, nekobox=269ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-97MS`
3. `AKUN-003-UNKNOWN-VLESS-WS-111MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS`
5. `AKUN-005-UNKNOWN-VLESS-WS-114MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-116MS`
8. `AKUN-008-090227-VLESS-WS-128MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-119MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-155MS`
11. `AKUN-014-CLOUDFLARE-VLESS-WS-135MS` (url=253ms, status=HTTP 204)
12. `AKUN-015-CLOUDFLARE-VLESS-WS-138MS` (url=343ms, status=HTTP 204)
13. `AKUN-016-CLOUDFLARE-VLESS-WS-156MS` (url=495ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-174MS` (url=356ms, status=HTTP 204)
15. `AKUN-018-CLOUDFLARE-VLESS-WS-134MS` (url=329ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-234MS` (url=445ms, status=HTTP 204)
17. `AKUN-022-CLOUDFLARE-VLESS-WS-218MS` (url=448ms, status=HTTP 204)
18. `AKUN-025-CLOUDFLARE-VLESS-WS-540MS` (url=539ms, status=HTTP 204)
19. `AKUN-027-CLOUDFLARE-VLESS-WS-461MS` (url=765ms, status=HTTP 204)
20. `AKUN-029-CLOUDFLARE-VLESS-WS-558MS` (url=961ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
