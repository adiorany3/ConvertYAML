# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-9889888-VLESS-WS-70MS` (url=216ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=203ms, nekobox=186ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS`
4. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=227ms, nekobox=181ms, status=no)
5. `AKUN-003-CLOUDFLARE-VLESS-WS-107MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-103MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS`
8. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS` (url=199ms, nekobox=178ms, status=no)
9. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS`
10. `AKUN-007-UNKNOWN-VLESS-WS-370MS`
11. `AKUN-008-UNKNOWN-VLESS-WS-69MS`
12. `AKUN-009-UNKNOWN-VLESS-WS-373MS`
13. `AKUN-015-CLOUDFLARE-VLESS-WS-410MS` (url=2465ms, nekobox=512ms, status=no)
14. `AKUN-010-CLOUDFLARE-VLESS-WS-425MS`
15. `AKUN-017-UNKNOWN-VLESS-WS-400MS` (url=4124ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-383MS` (url=847ms, status=HTTP 204)
17. `AKUN-019-MICROSOFT-VLESS-WS-389MS` (url=829ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-366MS` (url=756ms, status=HTTP 204)
19. `AKUN-024-ONTHEWIFI-VLESS-WS-731MS` (url=1253ms, status=HTTP 204)
20. `AKUN-034-DOGGOAPP-VLESS-WS-671MS` (url=2775ms, status=HTTP 204)
21. `AKUN-035-UNKNOWN-VLESS-WS-863MS` (url=3602ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
